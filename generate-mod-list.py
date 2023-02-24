import requests
import json

# 定义 mod ID
mod_id = "357540"

mod_loader = "fabric"

game_version = "1.18.2"
# 定义 cfwidget URL
url = f'https://api.cfwidget.com/{mod_id}?loader={mod_loader}&version={game_version}'

# 发送 GET 请求并获取响应
response = requests.get(url)

if response.status_code == 200:
    # 将响应内容解析为 JSON 对象
    response_json = response.json()
    # 获取 mod 的各种信息
    mod_urls = response_json['urls']
    mod_files = response_json['files'][0]
    mod_download = response_json['download']
    # 将 mod 的信息存储到一个 Python 字典中
    mod_info = {
        'urls': mod_urls,
        'files': mod_files,
        'downloads': mod_download
    }
    # 将 mod 信息写入 JSON 文件
    with open('mod-list.json', 'w') as f:
        json.dump(mod_info, f)
else:
    print('请求失败：', response.status_code)
