# -*- coding: utf-8 -*-
"""Audit Mandarin strings for translation.
Generates AUDIT_TERJEMAHAN.md in repository root.
"""
import pathlib, re, json, sys

root = pathlib.Path('.')
exclude_dirs = {'.git', '.venv', 'output', '__pycache__', 'node_modules', 'cache'}
# file extensions to scan (text based)
text_exts = {'.py', '.md', '.txt', '.html', '.htm', '.js', '.ts', '.jsx', '.tsx', '.vue', '.css', '.scss', '.ejs'}
pattern = re.compile(r'[\u4e00-\u9fff]')
entries = []

for p in root.rglob('*'):
    if not p.is_file():
        continue
    # skip excluded directories
    if any(part in exclude_dirs for part in p.parts):
        continue
    if p.suffix.lower() not in text_exts:
        continue
    try:
        text = p.read_text(encoding='utf-8')
    except Exception:
        continue
    for i, line in enumerate(text.splitlines(), start=1):
        for m in pattern.finditer(line):
            mand = m.group()
            # category heuristic
            if p.suffix.lower() in {'.html', '.htm', '.js', '.ts', '.jsx', '.tsx', '.vue', '.css', '.scss', '.ejs'}:
                cat = 'UI/GUI'
            elif p.suffix.lower() in {'.md', '.txt'}:
                if 'readme' in p.name.lower():
                    cat = 'Dokumen'
                else:
                    cat = 'Dokumen'
            elif 'config' in str(p).lower():
                cat = 'Config'
            elif 'prompt' in str(p).lower() or p.name.startswith('ai_'):
                cat = 'Prompt AI'
            elif 'notification' in str(p).lower():
                cat = 'Notifikasi'
            else:
                cat = 'Lainnya'
            # risk detection (simple)
            low = line.lower()
            risk = ''
            if any(keyword in low for keyword in ['api_key', 'token', 'secret', 'webhook', 'password', 'credential']):
                risk = 'YA'
            entries.append({
                'path': str(p),
                'line': i,
                'mandarin': mand,
                'category': cat,
                'risk': risk,
                'full_line': line.strip()
            })

# Summary calculations
total_files = sum(1 for p in root.rglob('*') if p.is_file() and not any(part in exclude_dirs for part in p.parts) and p.suffix.lower() in text_exts)
total_strings = len(entries)
cat_counts = {}
for e in entries:
    cat_counts.setdefault(e['category'], 0)
    cat_counts[e['category']] += 1

# Build markdown report
md = []
md.append('# AUDIT TERJEMAHAN - TrendRadar')
md.append('')
md.append('## Ringkasan pemindaian')
md.append(f'- Total berkas yang dipindai: **{total_files}**')
md.append(f'- Total string Mandarin terdeteksi: **{total_strings}**')
md.append('')
md.append('## Jumlah string per kategori')
md.append('| Kategori | Jumlah |')
md.append('|---|---|')
for cat, cnt in sorted(cat_counts.items(), key=lambda x: x[0]):
    md.append(f'| {cat} | {cnt} |')
md.append('')
md.append('## Contoh entri (maks 20)')
md.append('| Path | Baris | Mandarin | Usulan Bahasa Indonesia | Kategori | Risiko |')
md.append('|---|---|---|---|---|---|')
for e in entries[:20]:
    md.append(f"| {e['path']} | {e['line']} | {e['mandarin']} |  | {e['category']} | {e['risk']} |")
md.append('')
# Write file
report_path = root / 'AUDIT_TERJEMAHAN.md'
report_path.write_text('\n'.join(md), encoding='utf-8')
print('Audit report written to AUDIT_TERJEMAHAN.md')
