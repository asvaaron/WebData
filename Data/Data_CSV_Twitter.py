from Data_CSV import CSV_Manager
from ..Twitter.Tweet import Tweet
data=[]
class Data_CSV_Twitter( CSV_Manager ):

    def __init__(self, path):
        CSV_Manager.__init__(self, path)
        self.colnum = 0

    def set_colnum(self, colnum):
        self.colnum = colnum

    def append_tweet(self, Tweet):
        return None

    def make_columns_tweet(self):
        return None
