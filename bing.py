# 下载必应每日图片

import requests
import json
import urllib
import datetime
import time
import shutil
import stackprinter
import os

# 图片保存位置
path = os.path.split(os.path.realpath(__file__))[0] + os.sep


# 生成文件名
def getFileName(type):
    if type == 1:
        folder = "1080\\"
    elif type == 2:
        folder = "2k\\"
    else:
        folder = '4k\\'

    today = datetime.datetime.today()
    name = path + folder + str(today.year) + '-' + str(
        today.month) + '-' + str(today.day) + '.jpg'
    return name


# 下载图片并保存到指定路径
def download(url, type):
    global path
    print(url)
    name = getFileName(type)
    print(name)
    urllib.request.urlretrieve(url, name)


# 获取图片URL
def getUrl(resolution):
    if resolution == 1:
        width = 1920
        height = 1080
    elif resolution == 2:
        width = 2560
        height = 1440
    else:
        width = 3840
        height = 2560

    timeStamp = int(time.time())
    response = requests.get(
        'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&nc=' +
        str(timeStamp) + '&pid=hp&uhd=1&uhdwidth=' + str(width) +
        '&uhdheight=' + str(height)).text
    map = json.loads(response)

    return "https://cn.bing.com" + map["images"][0]["url"]


# 更新today.jpg
def updateImage():
    image = getFileName(1)
    backendImage = path + 'today.jpg'
    shutil.copy(image, backendImage)


# 检查目录是否存在，若不存在则创建
def checkDir():
    dir_1080 = path + "1080"
    dir_2k = path + "2k"
    dir_4k = path + "4k"
    if not os.path.isdir(dir_1080):
        os.makedirs(dir_1080)
    if not os.path.isdir(dir_2k):
        os.makedirs(dir_2k)
    if not os.path.isdir(dir_4k):
        os.makedirs(dir_4k)


def doWork():
    url = getUrl(1)
    download(url, 1)

    url = getUrl(2)
    download(url, 2)

    url = getUrl(4)
    download(url, 4)


if __name__ == "__main__":
    try:
        checkDir()
        doWork()
        updateImage()
    except BaseException as e:
        print(e)
        stackprinter.show()
