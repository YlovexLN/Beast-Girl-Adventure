import requests
import json

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'x-api-key': '$2a$10$54xio0nrZbsEiNfBLzq35.9NBvWrapx6UecXBQLnH9sHYuIiHGwJu'
}

# 读取mod_ids.json文件中的mod id到一个列表中
with open('mod-ids.json', 'r') as f:
    mod_ids = json.load(f)

all_mod_info = []  # 存储所有 mod 的信息

for mod_id in mod_ids:
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

with open('mod-list.json', 'w') as f:
    json.dump(all_mod_info, f)
