import json
from crawler.abstract_crawler import AbstractCrawler
from tools.steps.actions import action_dict


class GenericCrawler(AbstractCrawler):

    dataframe = None

    def __init__(self, type):
        super().__init__()
        self.type = type
        self.steps = json.loads(self.get_step(self.type))
        if self.steps is None:
            raise Exception("Step not found in Redis")

    def start(self):
        self.execute_before()
        self.execute_main()
        self.execute_after()
        self.save_data(self.dataframe)

    def execute_before(self):
        before = self.steps["script"]["before"]
        if before:
            for action in before:
                if action_dict[action] is None:
                    raise Exception("Action not found")
                action_dict[action](self.browser, before[action])
                return

    def execute_main(self):
        pass

    def execute_after(self):
        pass

    def extraction(self):
        pass
