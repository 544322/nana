import requests
from lxml import etree


#1.将目标网站上的页面抓取下来

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5702.400 QQBrowser/10.2.1893.400',
    'Referer':'https://img3.doubanio.com/misc/mixed_static/7c8d94cd9a093b03.css'

}

url='https://movie.douban.com/cinema/nowplaying/bozhou/'
response=requests.get(url,headers=headers)

text=response.text

#response.text 返回的是一个经过解码后的字符串，是str（uncode）类型
#response。content返回的是一个原生的字符串，是从网页上抓取下来的，没有经过处理的字符串，是bytes类型
#.2，将抓取的数据根据一定的规则进行提取

html= etree.HTML(text)    #解码
ul=html.xpath("//ul[@class='lists']")[0]
lis=ul.xpath("./li")
movies=[]
for li in lis:
    title=li.xpath("@data-title")[0]
    score=li.xpath("@data-score")[0]
    duration=li.xpath("@data-duration")[0]
    region=li.xpath("@data-region")[0]
    actors=li.xpath("@data-actors")[0]
    thumbnail=li.xpath(".//img/@src")[0]
    movie={
        'title':title,
        'score':score,
        'duration':duration,
        'region':region,
        'actors':actors,
        'thumbnail':thumbnail
    }
    movies.append(movie)
    print(movie)
    #print(thumbnail)
    #print(region)
    #print(title)
    #print(score)
    #print(duration)
    #print(etree.tostring(li, encoding='utf-8').decode('utf=8'))




