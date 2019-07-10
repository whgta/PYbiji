'''
访问一个网址
更改自己UserAgent进行伪装
'''

from urllib import request,error

if __name__ == '__main__':
    url = "http://www.baidu.com"

    try:

        # 使用head方法伪装UA
        #headers = {}
        #headers["User-Agent"] = "Mozilla/5.0 (iPhone; U; CPU iPhone OS 2_0 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5A347 Safari/52"
        #req = request.Request(url,headers=headers)

        # 使用add_header方法
        req = request.Request(url)
        req.add_header("User-Agent","Mozilla/5.0 (iPhone; U; CPU iPhone OS 2_0 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5A347 Safari/52")

        # 正常范围跟
        rsp = request.urlopen( req )
        html = rsp.read().decode()
        print(html)

    except error.HTTPError as e:
        print(e)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)

    print("DOne>.....")