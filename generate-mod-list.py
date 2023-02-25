import requests
import json

headers = {
    'Accept': 'application/json',
    'x-api-key': '$2a$10$54xio0nrZbsEiNfBLzq35.9NBvWrapx6UecXBQLnH9sHYuIiHGwJu'
}

mod_id = "301339"  # 替换为您要获取的mod的ID

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

    with open('mod-list.json', 'w') as f:
        json.dump(mod_info, f)
else:
    print(f"获取 mod {mod_id} 信息失败：{response.status_code}")
