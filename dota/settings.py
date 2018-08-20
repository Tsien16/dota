# -*- coding: utf-8 -*-

# Scrapy settings for dota project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'dota'

SPIDER_MODULES = ['dota.spiders']
NEWSPIDER_MODULE = 'dota.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'dota (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

COOKIE = {
	'__DAYU_PP': 'FAA2rRQMavv2eInRqunJ37f5b2236a1e',
	'_ga': 'GA1.2.1893565335.1533696130',
	'csrftoken': '6Wb41caf2Zcq7AgkuymwfoDI7q8asDLp',
	'_gid': 'GA1.2.2045171007.1534653832',
	'pkey': 'MTUzNDY4NjU4NS45OTE2NjAxMTMwMTg2XzF0YW95bnZqZXhzY3l5emFo',
	'Hm_lvt_575895fe09d48554a608faa5ef059555': '1534687858,1534711234,1534725984,1534731942',
	'cookie': '"gAJ9cQFVD2RqYW5nb190aW1lem9uZVULQXNpYS9IYXJiaW5zLg:1frday:iU0PabAL3DuogCia2U2mXWxPap4"',
	'_gat': '1',
	'Hm_lpvt_575895fe09d48554a608faa5ef059555': '1534747486',
}

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
		Chrome/68.0.3440.84 Safari/537.36',
	# 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	# 'Accept-Language': 'cn',
	'Host': 'dotamax.com',
	'Referer': 'http://dotamax.com/',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'dota.middlewares.DotaSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'dota.middlewares.DotaDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
	'dota.pipelines.MysqlTwistedPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


# 鑫哥：139249902， 307193116，
# 老朱：145997056
# 翔神 169688597
# 小唐 139063442
# 我 103853923，171732836
STEAM_ID = [139249902, 307193116, 145997056, 169688597, 139063442, 103853923, 171732836]

# mysql基本信息
MYSQL_HOST = "127.0.0.1"
MYSQL_DBNAME = "dota"
MYSQL_USER = "root"
MYSQL_PASSWORD = "15210931626"
