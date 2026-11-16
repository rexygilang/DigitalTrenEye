# -*- coding: utf-8 -*-
"""Generate detailed audit report for Mandarin strings.
Do NOT modify any project files except this report.
"""
import pathlib, re, json

root = pathlib.Path('.')
exclude_dirs = {'.git', '.venv', 'output', '__pycache__', 'node_modules', 'cache'}
# Text file extensions to scan
text_exts = {'.py', '.md', '.txt', '.html', '.htm', '.js', '.ts', '.jsx', '.tsx', '.vue', '.css', '.scss', '.ejs'}
# Pattern for any Chinese character
ch_pat = re.compile(r'[\u4e00-\u9fff]')
# Pattern to extract only Chinese characters from a line
only_ch = re.compile(r'([\u4e00-\u9fff]+)')

files_scanned = {}
entries = []

for p in root.rglob('*'):
    if not p.is_file():
        continue
    if any(part in exclude_dirs for part in p.parts):
        continue
    if p.suffix.lower() not in text_exts:
        continue
    try:
        text = p.read_text(encoding='utf-8')
    except Exception:
        continue
    file_count = 0
    for i, line in enumerate(text.splitlines(), start=1):
        if ch_pat.search(line):
            # extract consecutive Chinese substrings
            chinese_subs = only_ch.findall(line)
            if not chinese_subs:
                # no pure Chinese chars, skip (should not happen)
                continue
            mandarin = ' '.join(chinese_subs)
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
            # risk detection
            risk = ''
            risk_reason = ''
            low = line.lower()
            # 1. config keys (api_key, token, secret, webhook)
            if any(k in low for k in ['api_key', 'token', 'secret', 'webhook', 'password', 'credential']):
                risk = 'YA'
                risk_reason = 'kunci konfigurasi / token / webhook'
            # 2. platform ID or name (detect typical Chinese platform names)
            if any(name in line for name in ['微博', '微信', '知乎', '抖音', '今日头条', '热榜', '腾讯', '微博']):
                risk = 'YA'
                risk_reason = 'nama platform / ID'
            # 3. parsing markers (月, 日, 热度, etc.)
            if any(ch in line for ch in ['月', '日', '热度']):
                risk = 'YA'
                risk_reason = 'penanda parsing / regex'
            # 4. placeholder / format strings
            if '{' in line and '}' in line:
                risk = 'YA'
                risk_reason = 'placeholder / format'
            if '%s' in line or '%d' in line:
                risk = 'YA'
                risk_reason = 'placeholder / format'
            # 5. frequency_words file handling is outside this scan
            # Build entry
            usulan = 'TANYA' if risk == 'YA' else 'Terjemahan Indonesia (placeholder)'
            entries.append({
                'path': str(p),
                'line': i,
                'mandarin': mandarin,
                'usulan': usulan,
                'category': cat,
                'risk': risk,
                'risk_reason': risk_reason,
                'full_line': line.strip()
            })
            file_count += 1
    if file_count:
        files_scanned[str(p)] = file_count

# Build report
md = []
md.append('# AUDIT TERJEMAHAN - TrendRadar')
md.append('')
md.append('## Daftar berkas yang dipindai')
md.append('| Berkas | Jumlah string Mandarin |')
md.append('|---|---|')
for path, cnt in sorted(files_scanned.items()):
    md.append(f'| {path} | {cnt} |')
md.append('')
md.append('## Folder dikecualikan')
md.append(', '.join(sorted(exclude_dirs)))
md.append('')
md.append('## Ringkasan per kategori')
cat_counts = {}
for e in entries:
    cat_counts.setdefault(e['category'], 0)
    cat_counts[e['category']] += 1
md.append('| Kategori | Jumlah string |')
md.append('|---|---|')
for cat, cnt in sorted(cat_counts.items()):
    md.append(f'| {cat} | {cnt} |')
md.append('')
md.append('## Contoh entri (maks 20 baris)')
md.append('| Path | Baris | Mandarin | Usulan Bahasa Indonesia | Kategori | Risiko | Alasan Risiko |')
md.append('|---|---|---|---|---|---|---|')
for e in entries[:20]:
    md.append(f"| {e['path']} | {e['line']} | {e['mandarin']} | {e['usulan']} | {e['category']} | {e['risk']} | {e['risk_reason']} |")
md.append('')
md.append('## Ringkasan risiko')
risk_counts = {'kunci':0,'platform':0,'parsing':0,'placeholder':0}
for e in entries:
    if e['risk'] == 'YA':
        if 'kunci' in e['risk_reason']:
            risk_counts['kunci'] += 1
        if 'platform' in e['risk_reason']:
            risk_counts['platform'] += 1
        if 'parsing' in e['risk_reason']:
            risk_counts['parsing'] += 1
        if 'placeholder' in e['risk_reason']:
            risk_counts['placeholder'] += 1
md.append('| Tipe Risiko | Jumlah |')
md.append('|---|---|')
for k, v in risk_counts.items():
    md.append(f'| {k} | {v} |')
md.append('')
md.append('**Catatan**: Kolom "Usulan Bahasa Indonesia" berisi placeholder kecuali untuk entri berisiko yang ditandai "TANYA". Silakan review dan beri persetujuan untuk melanjutkan ke tahap eksekusi.')

report_path = pathlib.Path('AUDIT_TERJEMAHAN.md')
report_path.write_text('\n'.join(md), encoding='utf-8')
print('Report written')
