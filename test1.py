import requests

cookies = {
    '_ga_9VDZP6D43D': 'GS1.1.1650965503.1.1.1650966561.0',
    '_gid': 'GA1.3.1438726315.1651471700',
    'MoodleSession': 'e2id4jetvbdlcann9mi932egv8',
    '_gat_gtag_UA_227160516_1': '1',
    '_ga_T2DLCZMMH0': 'GS1.1.1651483569.13.1.1651484060.0',
    '_ga': 'GA1.3.885426599.1650965504',
}

headers = {
    'authority': 'kimjejl.atas.my.id',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    # 'cookie': '_ga_9VDZP6D43D=GS1.1.1650965503.1.1.1650966561.0; _gid=GA1.3.1438726315.1651471700; MoodleSession=e2id4jetvbdlcann9mi932egv8; _gat_gtag_UA_227160516_1=1; _ga_T2DLCZMMH0=GS1.1.1651483569.13.1.1651484060.0; _ga=GA1.3.885426599.1650965504',
    'referer': 'https://kimjejl.atas.my.id/?redirect=0',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
}

params = {
    'id': '2',
}

response = requests.get('https://kimjejl.atas.my.id/course/view.php', params=params, cookies=cookies, headers=headers)
print(response.text)