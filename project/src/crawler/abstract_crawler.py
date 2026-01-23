from abc import ABC, abstractmethod

from project.src.tools.redis import RedisClient
from project.src.tools.mongodb import MongoConnection
from project.src.tools.browser_provider import BrowserProvider


class AbstractCrawler(ABC):

    def __init__(self):
        self.redis = RedisClient.get()
        self.mongo = MongoConnection()
        self.browser = BrowserProvider()

    @abstractmethod
    def execute_main(self):
        pass

    @abstractmethod
    def execute_before(self):
        pass

    @abstractmethod
    def execute_after(self):
        pass

    def get_step(self, key):
        steps = None
        try:
            steps = self.redis.get(key)
        except:
            print("Error getting data from Redis")
        return steps

    def save_data(self, data):
        try:
            self.mongo.save_dataframe(data)
        except:
            print("Error saving data to MongoDB")
