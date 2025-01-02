import re
class RecipeCrawler:
    def __init__(self, recipe_link):
        self.recipe_link = recipe_link
    
    def check_link_syntax(self):
        print(self.recipe_link)
        if re.fullmatch(r"https://jamilacuisine.ro/([\w-]+)-reteta-video/", self.recipe_link):
            return 1
        else : return 0