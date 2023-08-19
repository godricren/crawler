from urllib.request import urlopen, Request
from fake_user_agent import user_agent
from urllib.parse import quote
from urllib.parse import urlencode

args = input('Please input worlds you want search.')
# 多个参数用这种方法拼接url
parms = {
    'wd': args,
    'ie': 'utf_8'
}
# 单个参数直接转化代码
# quote(args)
# user_agent = user_agent('chrome')
# headers = {
#     'User-Agent': user_agent
# }
url = f'http://www.baidu.com/s?{urlencode(parms)}'
print(url)
#
# req = Request(url,headers=headers)
# response = urlopen(req)
# print(response.read().decode())

