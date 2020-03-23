# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy import Spider

class TrumpSpider(scrapy.Spider):
    name = 'trumpnew'
    allowed_domains = ['trumptwitterarchive.com']
    start_urls = ['http://d5nxcu7vtzvay.cloudfront.net/data/realdonaldtrump/2009.json',
                  'http://d5nxcu7vtzvay.cloudfront.net/data/realdonaldtrump/2010.json',
                  'http://d5nxcu7vtzvay.cloudfront.net/data/realdonaldtrump/2011.json',
                  'http://d5nxcu7vtzvay.cloudfront.net/data/realdonaldtrump/2012.json',
                  'http://d5nxcu7vtzvay.cloudfront.net/data/realdonaldtrump/2013.json',
                  'http://d5nxcu7vtzvay.cloudfront.net/data/realdonaldtrump/2014.json',
                  'http://d5nxcu7vtzvay.cloudfront.net/data/realdonaldtrump/2015.json',
                  'http://d5nxcu7vtzvay.cloudfront.net/data/realdonaldtrump/2016.json',
                  'http://d5nxcu7vtzvay.cloudfront.net/data/realdonaldtrump/2017.json',
                  'http://d5nxcu7vtzvay.cloudfront.net/data/realdonaldtrump/2018.json',
                  'http://d5nxcu7vtzvay.cloudfront.net/data/realdonaldtrump/2019.json',
                  'http://d5nxcu7vtzvay.cloudfront.net/data/realdonaldtrump/2020.json']

    def parse(self, response):
        jsonresponse=json.loads(response.body)

        for tweet in jsonresponse:
            yield{  
                    'text':tweet['text'],
                    'source': tweet['source'],
                    'id_str': tweet ['id_str'],
                    'created_at': tweet['created_at'],
                    'retweet_count':tweet['retweet_count'],
                    'favorite_count':tweet['favorite_count'],
                    'is_retweet':tweet['is_retweet']}
