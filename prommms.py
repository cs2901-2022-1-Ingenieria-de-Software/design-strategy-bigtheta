from strategy import Strategy

class prommms(Strategy):
    def __init__(self):
        pass #initialize
    def execute(self,df):
        average = df['High'].rolling(7).mean()
        return average[5707]