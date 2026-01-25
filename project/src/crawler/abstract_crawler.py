from abc import ABC, abstractmethod

from tools.redis import RedisClient
from tools.mongodb import MongoConnection
from tools.browser_provider import BrowserProvider


class AbstractCrawler(ABC):

    def __init__(self):
        self.redis = RedisClient.get()
        self.mongo = MongoConnection()
        self.browser = BrowserProvider().get_browser()

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
            # steps = self.redis.get(key)
            # steps = self.redis.hgetall(key)
            steps = self.redis.execute_command("JSON.GET", key)
        except Exception as e:
            print("Error getting data from Redis", e)
        return steps

    def save_data(self, data):
        try:
            self.mongo.save_dataframe(data)
        except Exception as e:
            print("Error saving data to MongoDB", e)
