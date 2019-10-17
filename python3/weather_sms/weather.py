import requests

# API文档 https://lbs.amap.com/api/webservice/guide/api/weatherinfo/#t1
# 城市代码表：https://lbs.amap.com/api/webservice/download

# key是高德开放平台申请的key，在这里查看 https://lbs.amap.com/dev/key/app
key = 'xxxxxxxxxxxxxx'
city = '110000'
extensions = 'all'


def getTodayWeather():
    '''
        获取当天天气预报
    '''
    url = 'https://restapi.amap.com/v3/weather/weatherInfo?key=%s&city=%s&extensions=%s&output=json' % (
        key, city, extensions)
    r = requests.get(url)
    result = r.json()

    try:
        today = result['forecasts'][0]['casts'][0]
        return today
    except BaseException as e:
        print(e)
    return {}


def resolveWeather(w):
    # print(json.dumps(w, ensure_ascii=False))

    r = '今日天气：白天：%s，%s风%s级，夜间：%s，%s风%s级。 最高温度：%s℃ ,最低温度：%s℃' % (
        w['dayweather'], w['daywind'], w['daypower'], w['nightweather'],
        w['nightwind'], w['nightpower'], w['daytemp'], w['nighttemp'])

    return r
