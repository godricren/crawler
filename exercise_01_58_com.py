from urllib.request import Request, urlopen
from fake_user_agent import user_agent
from urllib.parse import quote
import time

args = input('Please input the bound.')
for page in range(1,4):
    url = f'https://dl.58.com/ershouche/pn{page}/?key={quote(args)}'
    print(url)
    time.sleep(2)
    ua = user_agent('chrome')
    headers = {
        'User-Agent': ua
    }
    req = Request(url,headers=headers)
    response = urlopen(req)
    print(response.getcode())
