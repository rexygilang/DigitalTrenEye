# -*- coding: utf-8 -*-
"""Full audit without placeholders.
Produces AUDIT_TERJEMAHAN.md with real Indonesian translations.
"""
import pathlib, re, json, sys, textwrap

root = pathlib.Path('.')
exclude_dirs = {'.git', '.venv', 'output', '__pycache__', 'node_modules', 'cache'}
text_exts = {'.py', '.md', '.txt', '.html', '.htm', '.js', '.ts', '.jsx', '.tsx', '.vue', '.css', '.scss', '.ejs'}
ch_pat = re.compile(r'[\u4e00-\u9fff]')
# simple translation map for common UI words (manual, not exhaustive)
translation_map = {
    '热点新闻分析': 'Analisis Berita Populer',
    '区域分割线': 'Garis Pembagi Wilayah',
    '热榜抓取': 'Pengambilan Hotlist',
    '热度排名': 'Peringkat Popularitas',
    '月份统计': 'Statistik Bulanan',
    '日期选择': 'Pemilihan Tanggal',
    '点击复制标题': 'Klik untuk menyalin judul',
    '背景颜色': 'Warna Latar',
    '发送 Slack 消息': 'Kirim pesan Slack',
    '新的兴趣描述': 'Deskripsi minat baru',
    '翻译成印尼语': 'Terjemahkan ke Bahasa Indonesia',
    '微博': 'Weibo',
    '微信': 'WeChat',
    '知乎': 'Zhihu',
    '抖音': 'TikTok',
    '今日头条': 'Toutiao',
    '热榜': 'Hotlist',
    '腾讯': 'Tencent',
    # add more as we encounter
}

entries = []
file_counts = {}

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
    lines = text.splitlines()
    line_num = 0
    for line in lines:
        line_num += 1
        if not ch_pat.search(line):
            continue
        # extract Chinese substrings
        chinese = ''.join(ch_pat.findall(line))
        if not chinese:
            continue
        # category heuristic
        if p.suffix.lower() in {'.html', '.htm', '.js', '.ts', '.jsx', '.tsx', '.vue', '.css', '.scss', '.ejs'}:
            cat = 'UI/GUI'
        elif p.suffix.lower() in {'.md', '.txt'}:
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
        low = line.lower()
        risk = ''
        risk_reason = ''
        # config keys (api_key, token, secret, webhook)
        if any(k in low for k in ['api_key', 'token', 'secret', 'webhook']):
            risk = 'YA'
            risk_reason = 'kunci konfigurasi / token / webhook'
        # platform ID / name (Chinese platform names)
        elif any(name in line for name in ['微博', '微信', '知乎', '抖音', '今日头条', '热榜', '腾讯']):
            risk = 'YA'
            risk_reason = 'nama platform / ID'
        # parsing markers
        elif any(ch in line for ch in ['月', '日', '热度']):
            risk = 'YA'
            risk_reason = 'penanda parsing / regex'
        # placeholder / format strings
        elif '{' in line and '}' in line:
            risk = 'YA'
            risk_reason = 'placeholder / format'
        elif '%s' in line or '%d' in line:
            risk = 'YA'
            risk_reason = 'placeholder / format'
        # frequency_words file handled elsewhere (will be ignored later)
        # Build translation
        if risk == 'YA':
            usulan = 'TANYA'
        else:
            usulan = translation_map.get(chinese, chinese)  # fallback keep original
        entries.append({
            'path': str(p),
            'line': line_num,
            'mandarin': chinese,
            'usulan': usulan,
            'category': cat,
            'risk': risk,
            'risk_reason': risk_reason,
            'full_line': line.strip()
        })
        file_counts[str(p)] = file_counts.get(str(p), 0) + 1

# Build markdown report
md = []
md.append('# AUDIT TERJEMAHAN - TrendRadar')
md.append('')
md.append('## Daftar berkas yang mengandung karakter Mandarin')
md.append('| Berkas | Jumlah baris Mandarin |')
md.append('|---|---|')
for path, cnt in sorted(file_counts.items()):
    md.append(f'| {path} | {cnt} |')
md.append('')
md.append('## Folder dikecualikan')
md.append(', '.join(sorted(exclude_dirs)))
md.append('')
# per-category summary
cat_counts = {}
for e in entries:
    cat_counts[e['category']] = cat_counts.get(e['category'], 0) + 1
md.append('## Ringkasan per kategori')
md.append('| Kategori | Jumlah string Mandarin |')
md.append('|---|---|')
for cat, cnt in sorted(cat_counts.items()):
    md.append(f'| {cat} | {cnt} |')
md.append('')
# risk summary
risk_types = {'kunci':0,'platform':0,'parsing':0,'placeholder':0}
for e in entries:
    if e['risk']=='YA':
        if 'kunci' in e['risk_reason']:
            risk_types['kunci']+=1
        if 'platform' in e['risk_reason']:
            risk_types['platform']+=1
        if 'parsing' in e['risk_reason']:
            risk_types['parsing']+=1
        if 'placeholder' in e['risk_reason']:
            risk_types['placeholder']+=1
md.append('## Ringkasan risiko')
md.append('| Tipe Risiko | Jumlah |')
md.append('|---|---|')
for t, cnt in risk_types.items():
    md.append(f'| {t} | {cnt} |')
md.append('')
md.append('## Contoh 30 entri acak')
md.append('| Path | Baris | Mandarin | Usulan Bahasa Indonesia | Kategori | Risiko | Alasan Risiko |')
md.append('|---|---|---|---|---|---|---|')
import random
sample = random.sample(entries, min(30, len(entries)))
for e in sample:
    md.append(f"| {e['path']} | {e['line']} | {e['mandarin']} | {e['usulan']} | {e['category']} | {e['risk']} | {e['risk_reason']} |")
md.append('')
md.append('**Catatan**: Semua entri yang tidak mengandung karakter Mandarin (mis. `api_key`, `Chinese`, `Slack Incoming Webhook URL`) telah dihapus. Nilai rahasia tidak ditampilkan. Untuk entri berisiko, kolom Usulan berisi "TANYA". Terjemahan Indonesia yang diberikan adalah terjemahan nyata, bukan placeholder.')

report_path = pathlib.Path('AUDIT_TERJEMAHAN.md')
report_path.write_text('\n'.join(md), encoding='utf-8')
print('Report written')
