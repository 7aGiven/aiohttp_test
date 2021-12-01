try:
    from aiohttp import ClientSession,ClientTimeout
except:
    from subprocess import run as shell
    shell(['apt','update'])
    shell(['apt','install','python3-pip','-y'])
    shell(['pip','install','aiohttp[speedups]'])
    from aiohttp import ClientSession,ClientTimeout
import asyncio



class data():
    def __init__(self,json:dict,text:str):
        self.text=text
        self.json=json
def 测试(method:str,url:str,header:str,body:str=None,proxy:str=None)->data:
    headers={}
    for h in header.splitlines():
        x=h.split(': ')
        headers[x[0]]=x[1]
    async def main():
        async with ClientSession(headers=headers,timeout=ClientTimeout(None))as client:
            async with client.request(method,url,data=body,proxy=proxy)as res:
                try:
                    result=data(await res.json(),await res.text())
                except:
                    print(await res.text())
        return result
    return asyncio.run(main())
def 测试get(url:str,header:str,proxy:str=None)->data:
    return 测试('GET',url,header,proxy=proxy)
def 测试post(url:str,header:str,body:str,proxy:str=None)->data:
    return 测试('POST',url,header,body,proxy)



def 单线程爬数据get(url:str,header:str,handle,var:list,proxy:str=None)->list:
    headers={}
    for h in header.splitlines():
        x=h.split(r': ')
        headers[x[0]]=x[1]
    async def main():
        result=[]
        async with ClientSession(headers=headers)as client:
            for x in var:
                print(x)
                async with client.get(url.format(x),proxy=proxy)as res:
                    try:
                        result.extend(handle(await res.text(),await res.json()))
                        await asyncio.sleep(0.5)
                    except:
                        print(await res.text())
                        continue
                print(len(result))
        return result
    return asyncio.run(main())

def 单线程爬数据post(url:str,header:str,body:str,handle,var:list,proxy:str=None)->list:
    headers={}
    for h in header.splitlines():
        x=h.split(r': ')
        headers[x[0]]=x[1]
    async def main():
        result=[]
        async with ClientSession(headers=headers)as client:
            for x in var:
                print(x)
                async with client.post(url,data=body.format(x),proxy=proxy)as res:
                    try:
                        result.extend(handle(await res.text(),await res.json()))
                        await asyncio.sleep(0.5)
                    except:
                        print(await res.text())
                        continue
                print(len(result))
        return result
    return asyncio.run(main())