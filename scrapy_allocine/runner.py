from scrapy.cmdline import execute

try:
    execute(
        [
            'scrapy',
            'crawl',
            'allocine',
        ]
    )
except SystemExit:
    pass