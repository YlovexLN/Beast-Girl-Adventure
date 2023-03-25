import os
import configparser
import json

# 获取config.ini文件的绝对路径
config_path = os.path.join(os.path.dirname(__file__), '..', 'config.ini')

# 读取config.ini文件
config = configparser.ConfigParser()
config.read(config_path, encoding='utf-8')

# 游戏版本
Version = config.get('Game', 'Version')

# Mod核心
ModLoader = config.get('Game', 'ModLoader')


# 从文件读取 mod-info.json
with open('mod-info.json', 'r') as f:
    all_mod_info = json.load(f)

# 过滤 mod 信息
filtered_mod_info = []

for mod_info in all_mod_info:
    mod_latest_files = mod_info['latestFiles']
    filtered_latest_files = []
    for latest_file in mod_latest_files:
        if Version in latest_file['gameVersions'] and ModLoader in latest_file['gameVersions']:
            game_versions = latest_file['gameVersions']
            if isinstance(game_versions, list):
                game_versions = ''.join(game_versions)
            game_version_start_index = game_versions.find('{Forge')
            if game_version_start_index != -1:
                game_version_end_index = game_versions.find(
                    '}', game_version_start_index) + 1
                # 提取 gameVersions 中满足条件的版本段
                filtered_game_versions = game_versions[game_version_start_index:game_version_end_index]
                # 添加到最新文件列表中
                filtered_latest_file = latest_file.copy()
                filtered_latest_file['gameVersions'] = filtered_game_versions
                filtered_latest_files.append(filtered_latest_file)

    if len(filtered_latest_files) == 0:
        continue

    # 添加满足条件的最新文件列表到 mod 信息中
    filtered_mod_info.append(mod_info.copy())
    filtered_mod_info[-1]['latestFiles'] = filtered_latest_files
