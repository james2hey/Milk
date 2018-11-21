import pickle

MIN = 0


class Cup:
    def __init__(self):
        self.filled_level = MIN
        self.size = 4

    def pour(self):
        self.filled_level += 1
        if self.filled_level > self.size:
            self.spill()
        return self.filled_level

    def spill(self):
        self.filled_level = MIN
        self.downgrade_cup()

    def upgrade_cup(self):
        self.size += 1

    def downgrade_cup(self):
        self.size -= 1

    def drink(self):
        if self.filled_level == self.size:
            self.size += 1
            self.filled_level = MIN
            return True
        else:
            self.filled_level = MIN
            return False

    def draw(self):
        string = "```\n"
        i = 3 * self.size
        string += i * "_" + "\n" if self.filled_level == self.size else "\n"

        i -= 2
        indent = 0
        while i >= self.size:
            string += indent * " " + "\\"
            # if bottom of cup or at the milk level
            if i == self.size or self.size - indent == self.filled_level + 1:
                string += i * "_" + "/\n"
            else:
                string += i * " " + "/\n"
            indent += 1
            i -= 2

        string += "```"
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
