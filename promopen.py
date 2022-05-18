from strategy import *

class promopen(Strategy):
    def __init__(self):
        pass
    def execute(self,df):
        average = df['Open'].mean()
        return average
