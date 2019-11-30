'''
作者:lg
日期:2019/10/12
文件描述:
缺陷：
'''
# ('1', '肖申克的救赎', '9.7', '1641722人')

import re
from urllib.request import urlopen


def getPage(url):
    response = urlopen(url)
    return response.read().decode('utf-8')


def parsePage(s):
    # findall实现:
    # ret = re.findall(
    #     '<ol class="grid_view">.*?<div class="item">.*?<em class="">(?P<id>\d+).*?<span class="title">(?P<title>.*?)</span>.*?"v:average">(?P<rating_num>\d+.\d).*?property="v:best".*?<span>(?P<comment_num>.*?)评价',
    #     s, re.S
    # )
    # return ret
    # finditer实现:

    str_compile = re.compile(
        '<ol class="grid_view">.*?<div class="item">.*?<em class="">(?P<id>\d+).*?<span class="title">(?P<title>.*?)</span>.*?"v:average">(?P<rating_num>\d+.\d).*?property="v:best".*?<span>(?P<comment_num>.*?)评价',
        re.S)
    ret = str_compile.finditer(s)

    for i in ret:
        yield {
            "id": i.group("id"),
            "title": i.group("title"),
            "rating_num": i.group("rating_num"),
            "comment_num": i.group("comment_num"),
        }


def main(num):
    url = 'https://movie.douban.com/top250?start=%s&filter=' % num
    response_html = getPage(url)
    ret = parsePage(response_html)
    for i in ret:
        print(i)



count = 0
for i in range(10):  # 10页
    main(count)
    count += 25

# url从网页上把代码搞下来
# bytes decode ——> utf-8 网页内容就是我的待匹配字符串
# ret = re.findall(正则，带匹配的字符串)  #ret是所有匹配到的内容组成的列表
