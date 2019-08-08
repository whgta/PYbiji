'''
处理js加密代码
'''

'''
通过查找，能找到js代码中操作代码

1. 这个是计算salt的公式 r = "" + ((new Date).getTime() + parseInt(10 * Math.random(),10);
2. sign: n.md5("fanyideskweb" + t + r + "ebSeFb%=XZ%T[KZ]c(sy!");
md5一共需要四个参数，第一个呵第四个都是固定值的字符串，第三个是所谓的salt
第二个参数就是输入的要查找的单词
'''

def getSalt():
    '''
    salt的公式 r = "" + ((new Date).getTime() + parseInt(10 * Math.random(),10);
    把他翻译python 代码
    :return:
    '''

    import time, random

    salt = int(time.time()*1000) + random.randint(0,10)

    return salt
def getMD5(v):
    import hashlib
    md5 = hashlib.md5()
    # update 需要一共butes格式的参数
    md5.update(v.encode("utf-8"))
    sign = md5.hexdigest()

    return sign


