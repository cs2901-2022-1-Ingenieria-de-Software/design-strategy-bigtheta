from strategy import Strategy

class promclose(Strategy):
    def __init__(self):
        pass #initialize
    def execute(self,df):
        average = df['Close'].mean()
        return average