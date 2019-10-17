import weather
import zhenzismsclient as smsclient
import ssl
import uuid

ssl._create_default_https_context = ssl._create_unverified_context

# 使用榛子云短信平台发送短信
# 在下面这个网址创建应用可以获取到appId和appSecret
# http://sms_developer.zhenzikj.com/zhenzisms_user/index.html
sms_apiurl = 'https://sms_developer.zhenzikj.com'
sms_appId = 'xxxxx'
sms_appSecret = 'xxxxxxxxxx'

# 接收短信的手机号列表
phone_list = ['xxxxxxxxxxxxx']


def doWork():
    t = weather.getTodayWeather()
    msg = weather.resolveWeather(t)
    print(msg)
    sendSms(msg)


def sendSms(message):
    client = smsclient.ZhenziSmsClient(sms_apiurl, sms_appId, sms_appSecret)
    for phone in phone_list:
        random_uuid = uuid.uuid5(uuid.NAMESPACE_DNS, 'test')
        r = client.send(phone, message, random_uuid)
        print(r)


if __name__ == "__main__":
    doWork()
    # print '111111111111111111111111111111111111111111111111111111111111111111111111111111111111'