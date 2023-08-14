from urllib import request
from datetime import datetime
from random import randint

MAX_STEPS = 70000
MIN_STEPS = 80000
MAX_DISTANCE = 45000
MIN_DISTANCE = 50000

ACCESS_TOKEN = 'vk1.xxxxxx_xxxxxx'  # <------------- TOKEN HERE

steps = randint(MIN_STEPS, MAX_STEPS)
distance = randint(MIN_DISTANCE, MAX_DISTANCE)
date = datetime.today().strftime('%Y-%m-%d')
user_agent = 'VKAndroidApp/7.7-10445 (Android 11; SDK 30; arm64-v8a; Xiaomi M2003J15SC; ru; 2340x1080)'

print(request.urlopen(request.Request('https://api.vk.com/method/vkRun.setSteps?steps='+str(steps) +
                                      '&distance=' + str(distance) +
                                      '&date=' + date +
                                      '&access_token=' + ACCESS_TOKEN +
                                      '&v=5.131',
                                      headers={'User-Agent': user_agent})).read().decode('utf-8'))
