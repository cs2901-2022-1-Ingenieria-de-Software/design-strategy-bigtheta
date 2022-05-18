import pandas 

class Readcsv:
    def __init__(self):
        self.df = pandas.read_csv('gold.csv')
    def set_strategy(self,strategy):
        self.strategy = strategy
    def do_something(self):
        return self.strategy.execute(self.df)