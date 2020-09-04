
class Actor:

    def __init__(self, name):
        if name != "" and isinstance(name, str):
            self.actor_full_name = name
        else:
            self.actor_full_name = None

        self.actor_colleague = []

    def __repr__(self):
        return "<Actor {}>".format(self.actor_full_name)

    def __eq__(self, other):
        return self.actor_full_name == other.actor_full_name

    def __lt__(self, other):
        return self.actor_full_name < other.actor_full_name

    def __hash__(self):
        return hash(self.actor_full_name)

    def add_actor_colleague(self, colleague):
        self.actor_colleague.append(colleague)

    def check_if_this_actor_worked_with(self, colleague):
        if colleague in self.actor_colleague:
            return True
        return False

