from pandas import read_csv

class Readcsv:
    def __init__(self):
        self.df = read_csv('gold.csv')
    def set_strategy(self,strategy):
        self.strategy = strategy
    def do_something(self):
        return self.strategy.execute(self.df)