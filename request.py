import requests

cookies = {
    'csrftoken': 'FFkmQJTYj061rVo8USPZrHlapKDC3Grz',
    'ig_did': 'DC63FC49-F274-46F7-A652-F0CBA6CF2099',
    'ig_nrcb': '1',
    'mid': 'YvGkSQALAAEe6RYfOP7dkWJ1LR6X',
    'ds_user_id': '342243188',
    'datr': 'UKTxYn87n9mwyNs2b6DSEl0h',
    'shbid': '"1997\\054342243188\\0541699112873:01f77c0fd96cc70218dcb6e8a55282e10c0cfeee0de3a16376c6cab254ccb8548c03c6d9"',
    'shbts': '"1667576873\\054342243188\\0541699112873:01f7f6a2a92239701e0f98c4c61d3f84725ecd1590a04d0da22e8a28e4378978f224af4c"',
    'sessionid': '342243188%3A2L5Ymi0TMtBsHJ%3A26%3AAYdQ46dACyDWG7nxYFJWO49VbRNMxKIalzSX-kIyOGk',
    'rur': '"VLL\\054342243188\\0541699112959:01f7df53c34ff91c80da88791cfc6890448c2b1c61c12b09f32b177e249d80fc833a894f"',
}

headers = {
    'authority': 'www.instagram.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.8',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'csrftoken=FFkmQJTYj061rVo8USPZrHlapKDC3Grz; ig_did=DC63FC49-F274-46F7-A652-F0CBA6CF2099; ig_nrcb=1; mid=YvGkSQALAAEe6RYfOP7dkWJ1LR6X; ds_user_id=342243188; datr=UKTxYn87n9mwyNs2b6DSEl0h; shbid="1997\\054342243188\\0541699112873:01f77c0fd96cc70218dcb6e8a55282e10c0cfeee0de3a16376c6cab254ccb8548c03c6d9"; shbts="1667576873\\054342243188\\0541699112873:01f7f6a2a92239701e0f98c4c61d3f84725ecd1590a04d0da22e8a28e4378978f224af4c"; sessionid=342243188%3A2L5Ymi0TMtBsHJ%3A26%3AAYdQ46dACyDWG7nxYFJWO49VbRNMxKIalzSX-kIyOGk; rur="VLL\\054342243188\\0541699112959:01f7df53c34ff91c80da88791cfc6890448c2b1c61c12b09f32b177e249d80fc833a894f"',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/p/CkY2BidPb7s/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'x-asbd-id': '198387',
    'x-csrftoken': 'FFkmQJTYj061rVo8USPZrHlapKDC3Grz',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': 'hmac.AR00ayg38eie91l4woc2ghVOahWpDZGwcqvDLbmwd2MMjOum',
    'x-instagram-ajax': '1006543976',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'comment_text': 'hello',
}

response = requests.post('https://www.instagram.com/api/v1/web/comments/2961354355224985324/add/', cookies=cookies, headers=headers, data=data)