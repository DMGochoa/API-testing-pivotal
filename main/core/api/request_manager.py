import requests
from main.core.utils.json_reader import Json_Reader
from main.core.utils.logger import logging


class RequestManager:
    """Request Manager Class implementation"""

    __instance = None

    def __init__(self, config_file=""):
        """Constructor For Request Manager

        Args:
            config_file (str, optional): json file with needed configuration. Defaults to ./configuration.json.
        """
        if config_file == "":
            self.__config = Json_Reader().open_json("./configuration.json")

        __environment = Json_Reader().open_json("./environment.json")

        env_selected = self.__config.get("environment", "development")
        self.__env_users = __environment.get(env_selected).get("users")
        self.headers = {"Accept": __environment["headers"]}
        self.url = __environment.get(env_selected).get("url")
        self.key = self.__env_users.get("admin").get("key")
        self.token = self.__env_users.get("admin").get("token")
        self.response = None

    @staticmethod
    def get_instance():
        """Singleton implementation to return instance

        Returns: instance -> RequestManager
        """
        if RequestManager.__instance is None:
            RequestManager.__instance = RequestManager()
        return RequestManager.__instance

    def make_request(self, http_method, endpoint, payload=None, **kwargs):
        """central method to make a request

        Args:
            http_method (str): HTTP method
            endpoint (str): Endpoint to make request
            payload (dict, optional): body of the request. Defaults to None.
        Returns:
            request response object
        """
        logging.debug(f"Request {http_method} to {self.url}{endpoint}")
        self.response = requests.request(
            method=HttpMethods[http_method].value,
            url=f"{self.url}{endpoint}",
            headers=self.headers,
        )
        return self.response
