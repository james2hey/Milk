import pickle


class Cup:
    def __init__(self):
        self.filled_level = 0
        self.size = 4

    def pour(self):
        self.filled_level += 1
        if self.filled_level > self.size:
            self.spill()

    def spill(self):
        self.filled_level = 0

    def upgrade_cup(self):
        self.size += 1

    def downgrade_cup(self):
        self.size -= 1

    def draw(self):
        i = self.size
        string = "```"
        while i > 1:
            string += (self.size - i) * " " + "\\" + (2 * i) * " " + "/\n"
            i -= 1
        string += (self.size - i) * " " + (2 * (i+1)) * "-" + "```"
        return string


class FreezeMilk:
    """Persistent data storage"""
    def __init__(self, server):
        self.server = server
        self.stats = dict()

    def save_milk_stats(self):
        server_path = "stats/" + str(self.server.id) + ".p"

        with open(server_path, 'wb') as fp:
            pickle.dump(self.stats, fp)

    def get_milk_stats(self):
        server_path = "stats/" + str(self.server.id) + ".p"

        try:
            with open(server_path, 'rb') as fp:
                self.stats = pickle.load(fp)

        except IOError:  # File doesn't exist
            for member in self.server.members:
                self.stats[member] = Cup()
