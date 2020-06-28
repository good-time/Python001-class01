# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class SpidersPipeline:
    def process_item(self, item, spider):
        movie_name = item['movie_name']
        movie_type = item['movie_type']
        release_time = item['release_time']
        output = f'|{movie_name}|\t|{movie_type}|{release_time}|\n\n'
        with open('./maoyanMovies.csv', 'a+', encoding='utf-8') as article:
            article.write(output)
            article.close()
        return item
