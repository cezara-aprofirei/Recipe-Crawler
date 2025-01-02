import os
class FileHandler:
    def __init__(self, file_path=None, file_name=None):
        self.file_path = file_path
        self.file_name = file_name

       
    def create_shopping_list(self):
        with open(self.file_name, "w") as file :
            return file.name

    def check_shopping_list_path(self):
        if os.path.isfile(self.file_path):
            return 1
        else :
            return 0
