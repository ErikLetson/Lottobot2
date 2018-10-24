import steem

class Lottobot():

    """
    Class for the Lottobot main object.
    """

    def __init__(self, node, account):

        self.node = node
        self.account = account

        self.steem = steem.Steem()

        self.on = True

        self.entrants = []

        #timers
        self.entry_timer = 0
        self.passes = 0

    def check_for_entries(self):

        pass

    def declare_winner(self):

        if len(self.entrants) > 0:

            x = random.randint(0, len(self.entrants))

            self.winner = self.entrants[x]

        else:

            pass

    def mainloop(self):

        while self.on:

            if self.entry_timer == 10:

                self.entry_time = 0
                self.check_for_entries(self)

                self.passes += 1

            else:

                self.entry_timer += 1

            #end
            if self.passes == 100:

                self.passes = 0
                self.declare_winner()
