import scrapy
import time

class TpPySpider(scrapy.Spider):
    name = "tp.py"
    allowed_domains = ["eg.toothpick.com"]
    base_url='https://eg.toothpick.com/'
    custom_settings = {
        'DOWNLOAD_DELAY':3,
        'RANDOMIZE_DOWNLOAD_DELAY':True,
        'FEED_EXPORT_ENCODING': 'utf-8-sig',
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'toothpick.csv'
    }

    cookies = {
        'device_id': 'c65ab874-33e9-4f74-9062-04361c48bd2a',
        '_fbp': 'fb.1.1778775496759.25710183448191877',
        '_ga': 'GA1.1.2068567689.1778775497',
        '_clck': 'wz12h5%5E2%5Eg61%5E0%5E2325',
        'search_engine': 'opensearch',
        '_ga_11ZQLLZ3BE': 'GS2.1.s1778780648$o2$g1$t1778780649$j59$l0$h0',
        '_ga_0QSX1NMT6H': 'GS2.1.s1778780636$o2$g1$t1778780649$j47$l0$h0',
        '_clsk': '7buhha%5E1778780650530%5E3%5E1%5Er.clarity.ms%2Fcollect',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
        'cache-control': 'max-age=0',
        'dnt': '1',
        'priority': 'u=0, i',
        'referer': 'https://www.google.com/',
        'sec-ch-ua': '"Chromium";v="148", "Microsoft Edge";v="148", "Not/A)Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0',
        # 'cookie': 'device_id=c65ab874-33e9-4f74-9062-04361c48bd2a; _fbp=fb.1.1778775496759.25710183448191877; _ga=GA1.1.2068567689.1778775497; _clck=wz12h5%5E2%5Eg61%5E0%5E2325; search_engine=opensearch; _ga_11ZQLLZ3BE=GS2.1.s1778780648$o2$g1$t1778780649$j59$l0$h0; _ga_0QSX1NMT6H=GS2.1.s1778780636$o2$g1$t1778780649$j47$l0$h0; _clsk=7buhha%5E1778780650530%5E3%5E1%5Er.clarity.ms%2Fcollect',
    }
    def start_requests(self):

        with open('urls.txt', 'r',encoding='utf-8-sig') as f:
            urls = f.read().splitlines()
        for url in urls:
            yield scrapy.Request(url=(self.base_url + url).strip() ,headers=self.headers,cookies=self.cookies)
            
            time.sleep(5)
    def parse(self, response):
        

        name= ''.join(response.xpath('//h1[@class=" text-2xl lg:text-4xl font-medium flex items-center gap-2 flex-grow"]//text()').getall()).strip()
        category= ''.join(response.xpath('//a[@class="text-primary-40 font-semibold"]//text()').getall()).strip()
        price=''.join(response.xpath('//h3[@class="Title-module__lv8BIG__large  !font-medium !font-medium text-primary-40"]//text()').getall()).strip()
        brand= ''.join(response.xpath('(//p[@class="ProductStyles-module__qXM31a__supplierAndBrandName"])[2]//text()').getall()).strip()
        sold_by= ''.join(response.xpath('(//p[@class="ProductStyles-module__qXM31a__supplierAndBrandName"])[1]//text()').getall()).strip()

        data={
            'name':name,
            'category':category,
            'price':price,
            'brand':brand,
            'sold_by':sold_by,
        }

        yield data
        print(data)
        
        