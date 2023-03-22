import json

class Json_Reader:
    def __init__(self, path):
        """In this implementation, the json_handler class takes a path parameter as 
        an argument during initialization. This is the path where the json file is.

        Args:
            path (str): Is the path where the json file is
        """
        self.path = path
        self.json = None
    
    def open_json(self):
        """This function opens the json file and returns the content

        Returns:
            object: The content of the json file
        """
        with open(self.path, 'r') as f:
            self.json = json.load(f)
        return self.json
    
    def save_json(self, data):
        """This function saves the data in the json file

        Args:
            data (object): The data to save in the json file
        """
        with open(self.path, 'w') as f:
            json.dump(data, f, indent=4)
