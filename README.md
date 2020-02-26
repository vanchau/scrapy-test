# scrapy-test
Testing scrapy web crawler

Visits https://cookscope.herokuapp.com/ and clicks each recipe to collect following example data from the recipe page:

```json
{
"recipe": "Goat cheese salad",
"author": "Daren",
"description": "\"Light, healthy and so easy to prepare\"",
"categories": ["Vegetarian", "Salad", "Healthy", "Gluten-free"]
}
```

Run locally:

1. Install dependencies (virtual env recommended)
```
$ pip install -r requirements.txt
```
2. Install Chrome driver
```
$ sudo apt-get install chromium-chromedriver
```
3. Crawl and save data
```
scrapy-test/tutorial$ scrapy crawl recipes -o recipes.json
```
