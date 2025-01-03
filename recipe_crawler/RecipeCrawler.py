import re
import requests
import random
from bs4 import BeautifulSoup
class RecipeCrawler:
    def __init__(self, recipe_url):
        self.recipe_url = recipe_url
        self.html_content = None
        self.shopping_list = {}
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
        ]
    
    def check_link_syntax(self):
        print(self.recipe_url)
        if re.fullmatch(r"https://jamilacuisine.ro/([\w-]+)-reteta-video/", self.recipe_url):
            return 1
        else : return 0

    def fetch_html_from_recipe_link(self):
        request_response = requests.get(self.recipe_url, headers={"User-Agent" : random.choice(self.user_agents)})
        if request_response.status_code == 200:
            self.html_content = request_response.text
        else :
            print(request_response.status_code)
            print(f"Failed to fetch resources from recipe URL : {self.recipe_url}")

    def parse_html_and_extract_ingredients(self):
        soup = BeautifulSoup(self.html_content, 'html.parser')
        ingredients_list = [ingredient.text for ingredient in soup.find_all('li', class_= 'wprm-recipe-ingredient')]
        #extract ingredients and quantities and add to map


    
crawler = RecipeCrawler("https://jamilacuisine.ro/piftie-de-cocos-aromata-dietetica-si-bine-inchegata-reteta-video/")
crawler.fetch_html_from_recipe_link()
crawler.parse_html_and_extract_ingredients()