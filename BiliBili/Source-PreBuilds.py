import os
import requests

Github_Token = os.environ["PAT"]
Folder_Path = os.environ["Folder_Path"]

BiliBili_apk_url = "https://dl.hdslb.com/mobile/latest/android64/iBiliPlayer-bili.apk"

BiliBili_apk_response = requests.request("GET", BiliBili_apk_url)

with open(Folder_Path + "BiliBili.apk", "wb") as f:
    f.write(BiliBili_apk_response.content)

revanced_cli_url = "https://api.github.com/repos/zjns/revanced-cli/releases/latest"

revanced_cli_payload = {}
revanced_cli_headers = {
    'Authorization': 'Bearer ' + Github_Token
}

revanced_cli_response = requests.request("GET", revanced_cli_url, headers=revanced_cli_headers,
                                         data=revanced_cli_payload)

revanced_cli_data = revanced_cli_response.json()

# print(revanced_cli_data)

# 初始化变量以存储第一个 APK 和 JAR 的下载 URL
revanced_cli_jar_url = ""

# 确保响应是字典并且包含 'assets' 键
if isinstance(revanced_cli_data, dict) and 'assets' in revanced_cli_data:
    for asset in revanced_cli_data['assets']:
        if asset['name'].endswith('.jar') and not revanced_cli_jar_url:
            revanced_cli_jar_url = asset['browser_download_url']

        # 如果两个 URL 都找到了，就跳出循环
        if revanced_cli_jar_url:
            break

# 转换为字符串并打印
revanced_cli_jar_url_str = str(revanced_cli_jar_url)

# print(revanced_cli_jar_url_str)

revanced_cli_jar_url = revanced_cli_jar_url_str

revanced_cli_jar_response = requests.request("GET", revanced_cli_jar_url)

with open(Folder_Path + "revanced-cli.jar", "wb") as f:
    f.write(revanced_cli_jar_response.content)
