import pandas 

class Readcsv:
    def __init__(self):
        self.df = pandas.read_csv('gold.csv')
    def setStrategy(self,strategy):
        self.strategy = strategy
    def doSomething(self):
        return self.strategy.execute(self.df)