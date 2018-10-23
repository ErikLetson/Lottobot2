import steem

class Lottobot():

    """
    Class for the Lottobot main object.
    """

    def __init__(self, node, account):

        self.node = node
        self.account = account

        self.steem = steem.Steem()

    def mainloop(self):

        pass
