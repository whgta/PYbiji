'''
破解有道词典
'''

from urllib import request,parse

def youdao(key):

    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

    data = {

        "i": "g",
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "15636837701293",
        "sign": "a85a09d05c753ab0b220f6d4f20c374e",
        "ts": "1563683770129",
        "bv": "53539dde41bde18f4a71bb075fcf2e66",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME"
    }

    # 参数data需要bytes格式
    data = parse.urlencode(data).encode()

    headers = {
                    'Accept':'application/json,text/javascript,*/*;q=0.01',
                    'Accept-Encoding':'gzip,deflate',
                    'Accept-Language':'zh-CN,zh;q=0.9',
                    'Connection':'keep - alive',
                    'Content-Length':'237',
                    'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',
                    'Cookie':'OUTFOX_SEARCH_USER_ID=154332542@10.169.0.84:JSESSIONID=aaanPPoLuhzK_5c34ZsWw;OUTFOX_SEARCH_USER_ID_NCOO=2100657766.4783928;___rl__test__cookies=1563684181516',
                    'Host':'fanyi.youdao.com',
                    'Origin':'http://fanyi.youdao.com',
                    'Referer':'http://fanyi.youdao.com/',
                    'User-Agent':'Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/75.0.3770.142 Safari/537.36',
                    'X-Requested-With':'XMLHttpRequest',


    }

    req = request.Request(url=url,data=data,headers=headers)
    rsp = request.urlopen(req)
    html = read().decode()
    print(html)

if __name__ == '__main__':
    youdao("girl")
