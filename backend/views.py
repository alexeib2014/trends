from django.http import HttpResponse
import requests
import json
import datetime


def index(request):
    headers = { 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'max-age=0',
                'cookie': '__utmz=10102256.1536848314.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=10102256.1177165713.1536848314.1536848314.1536900472.2; __utmc=10102256; __utmb=10102256.4.10.1536900472; OGPC=19008104-1:19008076-2:; NID=138=S78KDDEHDfpiWx71c6hC1Is2MB1Ior0wofjhCHZS7_PUXUJbFAEwUnRypiA5DoaHwerctEKfw3RRQaI0vqdKJh6okJ3G5o1DSwU7v5fjfjpuqUuRnoJFOjU7_Zjbh5OTnlej-s5_zJT_yeseiItTa2bujr9Y0CcoHPA; 1P_JAR=2018-09-14-05',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/69.0.3497.81 Chrome/69.0.3497.81 Safari/537.36' }

    # response = requests.get('https://trends.google.com/trends/explore?q=postgres&geo=US', headers=headers)

    response = requests.get('https://trends.google.com/trends/api/explore?hl=en-US&tz=-180&req=%7B%22comparisonItem%22:%5B%7B%22keyword%22:%22postgres%22,%22geo%22:%22US%22,%22time%22:%22today+12-m%22%7D%5D,%22category%22:0,%22property%22:%22%22%7D&tz=-180', headers=headers)
    data = json.loads(str(response.content[5:], 'utf-8'))
    token = data['widgets'][0]['token']

    day = str(datetime.datetime.now().day)

    url = 'https://trends.google.com/trends/api/widgetdata/multiline?hl=en-US&tz=-180&req=%7B%22time%22:%222017-09-' + day + '+2018-09-' + day + '%22,%22resolution%22:%22WEEK%22,%22locale%22:%22en-US%22,%22comparisonItem%22:%5B%7B%22geo%22:%7B%22country%22:%22US%22%7D,%22complexKeywordsRestriction%22:%7B%22keyword%22:%5B%7B%22type%22:%22BROAD%22,%22value%22:%22postgres%22%7D%5D%7D%7D%5D,%22requestOptions%22:%7B%22property%22:%22%22,%22backend%22:%22IZG%22,%22category%22:0%7D%7D&token=' + token + '&tz=-180'
    response = requests.get(url, headers=headers)
    data = json.loads(str(response.content[5:], 'utf-8'))

    return HttpResponse("Hello, world. You're at the backend index.")