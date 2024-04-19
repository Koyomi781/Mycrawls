# Scrapy settings for music163 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "music163"

SPIDER_MODULES = ["music163.spiders"]
NEWSPIDER_MODULE = "music163.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "music163 (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'NMTID=00OL8Pdf5TdSqHTZk1Qg9Kp8Pv4ymkAAAGN04PoOw; _iuqxldmzr_=32; _ntes_nnid=ee049b7fa2d0056b2fb8c8475faaa2b5,1708650654657; _ntes_nuid=ee049b7fa2d0056b2fb8c8475faaa2b5; WEVNSM=1.0.0; WNMCID=oxbmzd.1708650655278.01.0; timing_user_id=time_ASzSM1f92B; _ga=GA1.1.1584874827.1711532729; _ga_C6TGHFPQ1H=GS1.1.1711543748.2.1.1711544278.0.0.0; WM_TID=02OP8woNRoRERAARQULRrI%2FjAsq3xV6Y; sDeviceId=YD-t%2FfFB1E6ZQdFRhEURQPUvNviBs7jwOQ%2F; ntes_utid=tid._.FyHwBAuuj3hEU1AABQeFvZr2Vo%252ByhORI._.0; JSESSIONID-WYYY=ojSIzabHIDR9MyJiu5kprh8cAAMJFDpuqsnGkhJKstljj%2B3YVEvQOgUeMAMsjzW1qcoW%2BBxHWHF3jxFI5N04qaczQ8Ez7YwgxHdfBKqlXC2TOnqQjZe9eaElvbwGR4fEuaDS9euMGaQrwujjwiOUbrYA6jmP%5CYuTE%2F%2FqNM1JNN0%5CMTbX%3A1712647988402; WM_NI=4oRZ%2By3MVmL6YbnhPn3seNm87Kqz%2FiI2hQOTprEARuCjQ2OkUg1sLcUcBxU%2BI3OkxbUbrGqXoe6BIcAs4b4j5gdSG86e5WKiba5WzEHlqQGRVgTFXR%2BjCJ2Oc78X9RHBVWw%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb6f3539cb58797d764aaef8eb6c14f928e9b83d17b899f989bc967b2bc8788ce2af0fea7c3b92af8b19ebbaa73f1939a8ecf3e9bbea289d366f1adabaff034f595bf9bae638beea8b2ce60b4ae8ba2d17f81b69fd3ce6197b9ff94cf6997bd8e99d8218bed818cfb6a97bebea8f454adbbfaa3cc6983adfc83b762f7b9acb4c634f6bbfbb8ca63a2bffbb8f94f8cb4bfb2c65a96b99ca7db5ae9b68dabb145a1e9f8b9bc5a8c9e9ab8f637e2a3',
    'origin': 'https://music.163.com',
    'referer': 'https://music.163.com/discover/toplist?id=3778678',
    'sec-ch-ua': '"Microsoft Edge";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "music163.middlewares.Music163SpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   "music163.middlewares.Music163DownloaderMiddleware": 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   "music163.pipelines.Music163Pipeline": 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
DOWNLOAD_TIMEOUT = 180
LOG_LEVEL = 'ERROR'