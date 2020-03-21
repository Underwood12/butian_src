import requests
import os
import re

print ('需要输入您登陆补天后的cookie值')
nums = int(input('请输入爬取链接数：'))
cookie = input('请输入cookie（btlc_ba52447ea424004a7da412b344e5e41a）:')
cid = int(input('请输入第一个漏洞cid：'))
url = 'https://www.butian.net/Loo/submit?cid='
cookies={'btlc_ba52447ea424004a7da412b344e5e41a':cookie}
headers = {'content-type': 'application/json','User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}

nums_1 = nums
with open('src_url_list.txt',mode='w') as f:
    f.truncate()
    f.close()
with open('src_list.txt',mode='w') as f1:
    f1.truncate()
    f1.close()
while(nums):
    nums -= 1
    url_1 = url+str(cid)
    response = requests.get(url=url_1,cookies=cookies,headers=headers)
#    print ('爬取链接：'+url_1)
    cid -= 1
    
#    with open('1.html',mode='wb') as f:
#        f.write(response.content)
    if re.findall('(?:"\svalue=")([\w\d\.\-\（\）\(\):/]+)(?:" />)',response.text):
        src = re.findall('(?:"\svalue=")([\w\d\.\-\（\）\(\):/]+)(?:" />)',response.text)
        src_name = src[0]+':'+src[1]+'\n'
        src_url = src[1]+'\n'
        src_url = src_url.encode()
        src_name = src_name.encode()
        with open('src_list.txt',mode='ab+') as file:
            file.write(src_name)
        with open('src_url_list.txt',mode='ab+') as file_url:
            file_url.write(src_url)
        print ('正在爬取第'+str(nums_1-nums)+'条')
    else:
        continue
