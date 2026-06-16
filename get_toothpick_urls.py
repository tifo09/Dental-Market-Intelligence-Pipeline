import requests
import lxml.etree as ET
import time
for i in range(1,94):

    cookies = {
        'device_id': 'c65ab874-33e9-4f74-9062-04361c48bd2a',
        '_fbp': 'fb.1.1778775496759.25710183448191877',
        '_ga': 'GA1.1.2068567689.1778775497',
        '_clck': 'wz12h5%5E2%5Eg62%5E0%5E2325',
        'search_engine': 'opensearch',
        '_ga_0QSX1NMT6H': 'GS2.1.s1779845170$o6$g1$t1779845318$j57$l0$h0',
        '_ga_11ZQLLZ3BE': 'GS2.1.s1779845169$o6$g1$t1779845318$j59$l0$h0',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
        'cache-control': 'max-age=0',
        'dnt': '1',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Chromium";v="148", "Microsoft Edge";v="148", "Not/A)Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0',
        # 'cookie': 'device_id=c65ab874-33e9-4f74-9062-04361c48bd2a; _fbp=fb.1.1778775496759.25710183448191877; _ga=GA1.1.2068567689.1778775497; _clck=wz12h5%5E2%5Eg62%5E0%5E2325; search_engine=opensearch; _ga_0QSX1NMT6H=GS2.1.s1779845170$o6$g1$t1779845318$j57$l0$h0; _ga_11ZQLLZ3BE=GS2.1.s1779845169$o6$g1$t1779845318$j59$l0$h0',
    }



    response = requests.get('https://eg.toothpick.com/en/products', cookies=cookies, headers=headers)


    dom = ET.HTML(response.text)
    containers = dom.xpath('//div[@class="border overflow-hidden border-outline border-opacity-15 rounded-xl w-full flex flex-col h-full text-on-surface"]//a/@href')
    with open('urls.txt','a') as f:
        for container in containers:
            f.write(f'{container}\n')

    time.sleep(5)