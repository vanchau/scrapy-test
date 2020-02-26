import scrapy
import time
from selenium import webdriver

class QuotesSpider(scrapy.Spider):
    name = "recipes"
    start_urls = ['https://cookscope.herokuapp.com/']

    def __init__(self):
        self.driver = webdriver.Chrome()

    def parse(self, response):
        self.driver.get(response.url)

        # Wait for the page to load
        time.sleep(5)

        # Number of recipes to crawl
        amount = len(self.driver.find_elements_by_css_selector('img.card-img'))
        i = 0

        while i < amount:
            # Done again each loop due to stale element reference error otherwise
            recipes = self.driver.find_elements_by_css_selector('img.card-img')
            
            recipes[i].click()

            # Wait for the page to load
            time.sleep(5)

            # Scrape
            yield {
                "recipe": self.driver.find_element_by_css_selector('div.recipe-card-title').text,
                "author": self.driver.find_element_by_css_selector('a.card-author').text,
                "description": self.driver.find_element_by_xpath('(//div[@class="card-body"]//p[@class="card-text"])[2]').text,
                # Formatting: "Dinner, Chicken, Soup" -> [Dinner, Chicken, Soup]
                "categories": [item.strip() for item in self.driver.find_element_by_css_selector('div.category-info').text.split(',')],
            }

            self.driver.back()

            # Wait for the page to load
            time.sleep(5)
            i += 1

        self.driver.close()