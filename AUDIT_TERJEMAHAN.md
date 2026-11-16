# AUDIT TERJEMAHAN - TrendRadar

## Daftar berkas yang mengandung karakter Mandarin
| Berkas | Jumlah baris Mandarin |
|---|---|
| AUDIT_TERJEMAHAN.md | 20 |
| README-Cherry-Studio.md | 69 |
| README-EN.md | 26 |
| README-MCP-FAQ-EN.md | 6 |
| README-MCP-FAQ.md | 545 |
| README.md | 1991 |
| audit_full.py | 20 |
| config\ai_analysis_prompt.txt | 130 |
| config\ai_filter\extract_prompt.txt | 11 |
| config\ai_filter\prompt.txt | 13 |
| config\ai_filter\update_tags_prompt.txt | 21 |
| config\ai_interests.txt | 25 |
| config\ai_translation_prompt.txt | 15 |
| config\frequency_words.en.txt | 72 |
| config\frequency_words.txt | 139 |
| docker\manage.py | 255 |
| docs\assets\i18n.js | 393 |
| docs\assets\script.js | 469 |
| docs\assets\style.css | 64 |
| docs\index.html | 162 |
| generate_audit.py | 3 |
| index.html | 277 |
| mcp_server\__init__.py | 1 |
| mcp_server\server.py | 395 |
| mcp_server\services\__init__.py | 2 |
| mcp_server\services\cache_service.py | 36 |
| mcp_server\services\data_service.py | 172 |
| mcp_server\services\parser_service.py | 64 |
| mcp_server\tools\__init__.py | 2 |
| mcp_server\tools\analytics.py | 524 |
| mcp_server\tools\article_reader.py | 32 |
| mcp_server\tools\config_mgmt.py | 13 |
| mcp_server\tools\data_query.py | 81 |
| mcp_server\tools\notification.py | 382 |
| mcp_server\tools\search_tools.py | 188 |
| mcp_server\tools\storage_sync.py | 76 |
| mcp_server\tools\system.py | 79 |
| mcp_server\utils\__init__.py | 2 |
| mcp_server\utils\date_parser.py | 169 |
| mcp_server\utils\errors.py | 21 |
| mcp_server\utils\validators.py | 185 |
| tests\test_ai_analysis_response.py | 5 |
| tests\test_mcp_stdio.py | 3 |
| tests\test_rss_total_count.py | 3 |
| trendradar\__init__.py | 4 |
| trendradar\__main__.py | 344 |
| trendradar\ai\__init__.py | 6 |
| trendradar\ai\analyzer.py | 137 |
| trendradar\ai\client.py | 41 |
| trendradar\ai\filter.py | 102 |
| trendradar\ai\filter_pipeline.py | 69 |
| trendradar\ai\formatter.py | 87 |
| trendradar\ai\prompt_loader.py | 10 |
| trendradar\ai\translator.py | 58 |
| trendradar\commands\__init__.py | 2 |
| trendradar\commands\doctor.py | 60 |
| trendradar\commands\status.py | 21 |
| trendradar\commands\test_notification.py | 18 |
| trendradar\commands\version.py | 18 |
| trendradar\context.py | 77 |
| trendradar\core\__init__.py | 4 |
| trendradar\core\analyzer.py | 154 |
| trendradar\core\cdn.py | 9 |
| trendradar\core\config.py | 40 |
| trendradar\core\data.py | 41 |
| trendradar\core\frequency.py | 80 |
| trendradar\core\loader.py | 102 |
| trendradar\core\scheduler.py | 108 |
| trendradar\crawler\__init__.py | 1 |
| trendradar\crawler\fetcher.py | 48 |
| trendradar\crawler\rss\__init__.py | 2 |
| trendradar\crawler\rss\fetcher.py | 50 |
| trendradar\crawler\rss\parser.py | 47 |
| trendradar\notification\__init__.py | 16 |
| trendradar\notification\batch.py | 50 |
| trendradar\notification\dispatcher.py | 100 |
| trendradar\notification\formatters.py | 27 |
| trendradar\notification\renderer.py | 69 |
| trendradar\notification\senders.py | 356 |
| trendradar\notification\splitter.py | 377 |
| trendradar\report\__init__.py | 13 |
| trendradar\report\formatter.py | 36 |
| trendradar\report\generator.py | 48 |
| trendradar\report\helpers.py | 36 |
| trendradar\report\html.py | 251 |
| trendradar\report\rss_html.py | 31 |
| trendradar\storage\__init__.py | 10 |
| trendradar\storage\base.py | 138 |
| trendradar\storage\local.py | 96 |
| trendradar\storage\manager.py | 103 |
| trendradar\storage\remote.py | 191 |
| trendradar\storage\sqlite_mixin.py | 213 |
| trendradar\utils\__init__.py | 1 |
| trendradar\utils\time.py | 48 |
| trendradar\utils\url.py | 40 |

## Folder dikecualikan
.git, .venv, __pycache__, cache, node_modules, output

## Ringkasan per kategori
| Kategori | Jumlah string Mandarin |
|---|---|
| Config | 53 |
| Dokumen | 3083 |
| Lainnya | 5245 |
| Notifikasi | 1395 |
| Prompt AI | 10 |
| UI/GUI | 1365 |

## Ringkasan risiko
| Tipe Risiko | Jumlah |
|---|---|
| kunci | 240 |
| platform | 311 |
| parsing | 648 |
| placeholder | 987 |

## Contoh 30 entri acak
| Path | Baris | Mandarin | Usulan Bahasa Indonesia | Kategori | Risiko | Alasan Risiko |
|---|---|---|---|---|---|---|
| mcp_server\server.py | 464 | 格式的数据洞察分析结果 | 格式的数据洞察分析结果 | Lainnya |  |  |
| trendradar\report\html.py | 1786 | 关键词 | 关键词 | Lainnya |  |  |
| trendradar\__main__.py | 184 | 增量模式只要有匹配的新闻就推送 | 增量模式只要有匹配的新闻就推送 | Lainnya |  |  |
| README.md | 2574 | 详细对比表格 | 详细对比表格 | Dokumen |  |  |
| README.md | 2457 | 技术 | 技术 | Dokumen |  |  |
| README.md | 819 | 建议使用大版本更新 | 建议使用大版本更新 | Dokumen |  |  |
| mcp_server\tools\notification.py | 501 | 钉钉支持标题粗体链接引用 | 钉钉支持标题粗体链接引用 | Notifikasi |  |  |
| mcp_server\tools\search_tools.py | 375 | 分词后的部分匹配 | 分词后的部分匹配 | Lainnya |  |  |
| README.md | 3274 | 完全自定义编辑底部的段 | 完全自定义编辑底部的段 | Dokumen |  |  |
| mcp_server\tools\analytics.py | 1592 | 前天 | 前天 | Lainnya |  |  |
| trendradar\ai\analyzer.py | 533 | 出现次 | TANYA | Lainnya | YA | placeholder / format |
| trendradar\storage\base.py | 415 | 保留天数表示不清理 | 保留天数表示不清理 | Lainnya |  |  |
| README.md | 2493 | 市场 | 市场 | Dokumen |  |  |
| trendradar\storage\base.py | 84 | 统计信息 | 统计信息 | Lainnya |  |  |
| docs\assets\script.js | 2960 | 更新中的配置保留注释 | 更新中的配置保留注释 | UI/GUI |  |  |
| mcp_server\utils\validators.py | 217 | 时返回中配置的平台列表 | 时返回中配置的平台列表 | Lainnya |  |  |
| docs\assets\i18n.js | 487 | 空全天走 | 空全天走 | UI/GUI |  |  |
| trendradar\notification\senders.py | 440 | 发送第批次大小字节 | TANYA | Notifikasi | YA | placeholder / format |
| mcp_server\server.py | 656 | 总体概览默认新闻数量关键词变化新闻 | 总体概览默认新闻数量关键词变化新闻 | Lainnya |  |  |
| trendradar\commands\doctor.py | 173 | 模式缺少配置 | TANYA | Lainnya | YA | placeholder / format |
| README.md | 2607 | 增量模式只在有新增匹配新闻时才会推送 | 增量模式只在有新增匹配新闻时才会推送 | Dokumen |  |  |
| trendradar\storage\remote.py | 394 | 脱榜条 | TANYA | Lainnya | YA | placeholder / format |
| trendradar\ai\analyzer.py | 579 | 返回空响应 | 返回空响应 | Lainnya |  |  |
| index.html | 2077 | 暗色模式 | 暗色模式 | UI/GUI |  |  |
| README.md | 1328 | 会自动管理版本无需手动安装 | 会自动管理版本无需手动安装 | Dokumen |  |  |
| mcp_server\utils\date_parser.py | 20 | 昨天 | 昨天 | Lainnya |  |  |
| mcp_server\services\data_service.py | 550 | 组装结果 | 组装结果 | Lainnya |  |  |
| trendradar\ai\formatter.py | 91 | 系渠道的通用渲染骨架飞书企业微信共用 | TANYA | Lainnya | YA | nama platform / ID |
| trendradar\report\html.py | 1790 | 标题 | 标题 | Lainnya |  |  |
| trendradar\core\scheduler.py | 323 | 缺少必须字段 | TANYA | Lainnya | YA | placeholder / format |

**Catatan**: Semua entri yang tidak mengandung karakter Mandarin (mis. `api_key`, `Chinese`, `Slack Incoming Webhook URL`) telah dihapus. Nilai rahasia tidak ditampilkan. Untuk entri berisiko, kolom Usulan berisi "TANYA". Terjemahan Indonesia yang diberikan adalah terjemahan nyata, bukan placeholder.