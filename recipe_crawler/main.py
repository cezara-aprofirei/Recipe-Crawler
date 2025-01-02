import FileHandler
import RecipeCrawler
if __name__ == "__main__":
    print("Welcome to Recipe Crawler! I'll make your grocery shopping list based on what recipes you want to follow. \n")
    list_type = int(input("To make a new list press 1, to add to an alredy existing list, press 2 : ").strip())

    while list_type not in {1, 2}:
        list_type = input("Invalid option! Please provide a valid number : ")

    if list_type == 1 :
        list_name = input("Please provide a name for your list :").strip()
        file_handler = FileHandler.FileHandler(file_name = list_name)
        list_path = file_handler.create_shopping_list()

    if list_type == 2:
        list_path = input("Please provide the path to your list : ").strip()
        file_handler = FileHandler.FileHandler(list_path)
        while not file_handler.check_shopping_list_path():
            list_path = input("The path you provided does not exist. Please provide the correct path to your list : ").strip()
            setattr(file_handler, "file_path", list_path)
        
    recipe = input("Please provide the link to the recipe for which you want to add the ingredients to your list using the following format : https://jamilacuisine.ro/{reteta}-reteta-video/").strip()
    while recipe :
        recipe_crawler = RecipeCrawler.RecipeCrawler(recipe)
        while not recipe_crawler.check_link_syntax():
            recipe = input("The recipe link you provided is incorrect. Please provide a new one : ").strip()
            setattr(recipe_crawler, "recipe_link", recipe)
    
        recipe = input("Would you like to add another recipe to the list ? Enter link : ")

