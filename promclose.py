from strategy import *

class promclose(Strategy):
    def __init__(self):
        pass
    def execute(self,df):
        average = df['Close'].mean()
        return average