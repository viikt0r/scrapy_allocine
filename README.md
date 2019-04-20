# Overview

This is a Scrapy project which can be used to crawl [allocine](http://www.allocine.fr/) website to scrape movies information and then store the data in json format.

## Installation
Clone the repo and navigate into scrapy_allocine folder.
```bash
git clone https://github.com/viikt0r/scrapy_allocine.git
cd scrapy_allocine
```

Start the crawler with runner.py.

```bash
python runner.py
```

Data will be stored in json file named movie.json located at scrapy_allocine/data/movie.json.
```bash
{
    "name": "Le Seigneur des anneaux : le retour du roi", 
    "press_rated": "3,8", 
    "users_rated": "4,5", 
    "short_description": "Les arm\u00e9es de Sauron ont attaqu\u00e9 Minas Tirith, la capitale de Gondor..."
}
```

## Stats 
```bash
{
 'downloader/request_bytes': 97593,
 'downloader/request_count': 321,
 'downloader/request_method_count/GET': 321,
 'downloader/response_bytes': 19426596,
 'downloader/response_count': 321,
 'downloader/response_status_count/200': 321,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2019, 4, 20, 15, 16, 21, 214354),
 'item_scraped_count': 290,
 'log_count/DEBUG': 611,
 'log_count/INFO': 9,
 'request_depth_max': 3,
 'response_received_count': 321,
 'robotstxt/request_count': 1,
 'robotstxt/response_count': 1,
 'robotstxt/response_status_count/200': 1,
 'scheduler/dequeued': 320,
 'scheduler/dequeued/memory': 320,
 'scheduler/enqueued': 320,
 'scheduler/enqueued/memory': 320,
 'start_time': datetime.datetime(2019, 4, 20, 15, 16, 6, 194388)
}
```

## Disclaimer
The project and the obtained dataset is intended only for educational purpose. It is completely open source and has no value intentions to commercialise complete or any part of the same. The developer is on no part the owner of any resources used and does not claim to hold the permissions to use the project.

## License
[MIT](https://choosealicense.com/licenses/mit/)