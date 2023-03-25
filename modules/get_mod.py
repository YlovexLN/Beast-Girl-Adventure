import os
import configparser
import requests
import json

# 获取config.ini文件的绝对路径
config_path = os.path.join(os.path.dirname(__file__), '..', 'config.ini')

# 读取config.ini文件
config = configparser.ConfigParser()
config.read(config_path, encoding='utf-8')

# API KEY
API_KEY = config.get('API', 'API_KEY')

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'x-api-key': API_KEY
}

mod_ids = config.get('Mod_id', 'Mod_ids').split(',')

# 游戏版本
Version = config.get('Game', 'Version')

# Mod核心
ModLoader = config.get('Game', 'ModLoader')

all_mod_info = []  # 存储所有 mod 的信息

for mod_id in mod_ids:
    # https://api.curseforge.com/ API接口
    url = f'https://api.curseforge.com/v1/mods/{mod_id}'

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # 将响应内容解析为 JSON 对象
        response_json = response.json()

        # 获取 data 里的信息
        mod_data = response_json['data']
        mod_id = mod_data['id']
        game_id = mod_data['gameId']
        mod_name = mod_data['name']
        mod_links_websiteUrl = mod_data['links']['websiteUrl']
        mod_latest_files = mod_data['latestFiles']

        # 提取 latestFiles 里的信息
        mod_latest_files_info = []
        for file in mod_latest_files:
            file_info = {
                'id': file['id'],
                'modid': file['modId'],
                'displayName': file['displayName'],
                'fileName': file['fileName'],
                'fileDate': file['fileDate'],
                'downloadUrl': file['downloadUrl'],
                'gameVersions': file['gameVersions']
            }
            mod_latest_files_info.append(file_info)

        # 将需要的信息存储到一个 Python 字典中
        mod_info = {
            'id': mod_id,
            'gameId': game_id,
            'name': mod_name,
            'links': mod_links_websiteUrl,
            'latestFiles': mod_latest_files_info
        }

        all_mod_info.append(mod_info)  # 将该 mod 的信息存储到总列表中
    else:
        print(f"获取 mod {mod_id} 信息失败：{response.status_code}")

with open('mod-info.json', 'w') as f:
    json.dump(all_mod_info, f, ensure_ascii=False, indent=4)
