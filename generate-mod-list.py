import requests
import json

# API KEY
API_KEY = '$2a$10$54xio0nrZbsEiNfBLzq35.9NBvWrapx6UecXBQLnH9sHYuIiHGwJu'

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'x-api-key': API_KEY
}

# 导入mod-ids.json文件
with open('mod-ids.json', 'r') as f:
    mod_ids = json.load(f)

# 游戏版本
Version = "1.16.5"

# mod核心
modLoader = "Forge"

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

        # 筛选最新文件的 gameVersions 中有 1.16.5 和 Forge 的版本
        filtered_latest_files = []
        for latest_file in mod_latest_files_info:
            if Version in latest_file['gameVersions'] and modLoader in latest_file['gameVersions']:
                game_versions = latest_file['gameVersions']
                if isinstance(game_versions, list):
                    game_versions = ''.join(game_versions)
                game_version_start_index = game_versions.find('{Forge')
                if game_version_start_index != -1:
                    game_version_end_index = game_versions.find(
                        '}', game_version_start_index) + 1
                    # 提取 gameVersions 中满足条件的版本段
                    filtered_game_versions = game_versions[game_version_start_index:game_version_end_index]
                    # 替换原来的 gameVersions
                    latest_file['gameVersions'] = filtered_game_versions
                filtered_latest_files.append(latest_file)

        mod_info['latestFiles'] = filtered_latest_files
        all_mod_info.append(mod_info)  # 将该 mod 的信息存储到总列表中
    else:
        print(f"获取 mod {mod_id} 信息失败：{response.status_code}")

with open('mod-list.json', 'w') as f:
    json.dump(all_mod_info, f, ensure_ascii=False, indent=4)
