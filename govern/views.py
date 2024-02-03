import datetime

from matplotlib import pyplot as plt
from wordcloud import WordCloud
import jieba
from django.shortcuts import render

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import requests

from core.models import Information
from .models import News,Last_update

web_index = {
    '广西': 'http://www.gxzf.gov.cn/gxyw/',
    '北京': 'https://www.beijing.gov.cn/ywdt/',
    '广东': 'https://www.gd.gov.cn/gdywdt/gdyw/index.html',
    '浙江': 'https://www.zj.gov.cn/col/col1545696/index.html',
    '重庆': 'http://www.cq.gov.cn/ywdt/',
    '四川': 'https://www.sc.gov.cn/10462/wza2012/zwxx/zwxx.shtml',
    '上海': 'https://www.shanghai.gov.cn/nw15343/index.html',
    '湖南': 'https://www.hunan.gov.cn/hnszf/hnyw/zwdt/szdt_sjpx.html',
    '湖北': 'https://www.hubei.gov.cn/szyw/',
    '河南': 'https://www.henan.gov.cn/ywdt/hnyw/',
    '山东': 'http://www.shandong.gov.cn/col/col97564/index.html',
    '江苏': 'https://www.jiangsu.gov.cn/col/col60096/index.html',
    '河北': 'https://www.hebei.gov.cn/hebei/14462058/14471802/14471750/index.html',
    '安徽': 'https://www.ah.gov.cn/zwyw/jryw/index.html',
}

news=[]

def get_information(city):
    wd = webdriver.Chrome()
    wd.minimize_window()
    wd.get(web_index[city])


    content = wd.find_elements(By.TAG_NAME, 'a')
    for c in content:
        if len(c.text) > 15 and '公网安备' not in c.text and 'ICP备' not in c.text:
            title = c.text
            link = c.get_attribute('href')
            date = datetime.datetime.now()
            news = News(title=title, link=link, update=date,city=city)
            news.save()

    l = Last_update(city=city,update=datetime.datetime.today().strftime('%Y-%m-%d'))
    l.save()



def get_news(request):

    username = request.user.username
    information = Information.objects.filter(name=username)[0]
    city = information.city
    try:
        day = Last_update.objects.filter(city=city)
        day = day[len(day) - 1].update.strftime('%Y-%m-%d')
    except:
        day = ''
        print("12312313123123")
    print(day, '\n', datetime.datetime.today().strftime('%Y-%m-%d'))
    if day != datetime.datetime.today().strftime('%Y-%m-%d'):
        get_information(city)

    notes = News.objects.filter(city=city)
    notes = notes[len(notes) - 10 :]

    return render(request, 'govern/governshow.html',{
        'notes': notes,
        'city': city,
    })

def cloud(request):
    text = ""
    username = request.user.username
    information = Information.objects.filter(name=username)[0]
    city = information.city
    notes = News.objects.filter(city=city)
    notes = notes[len(notes) - 10:]
    for note in notes:
        text += note.title + " "

    valid = ''
    seg_list = jieba.cut(text, cut_all=False)
    valid += " ".join(seg_list)

    wordcloud = WordCloud(font_path="simhei.ttf", background_color="white", width=800, height=600).generate(valid)

    # 显示词云
    # plt.imshow(wordcloud, interpolation="bilinear")
    # plt.axis("off")
    # plt.show()

    # 导出图片
    wordcloud.to_file('media/item_images/cloud.png')
    return render(request, 'govern/cloud.html',{
        'url': '/media/item_images/cloud.png'
    })

