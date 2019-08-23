class Friend:
    def __init__(self, fname):
        self.name = fname
        self.message = "No party..."
    def update(self, msg):
        self.message = msg
    def show_invite(self):
        return self.message

class Party:
    def __init__(self, party_name):
        self.name = party_name
        self.friends = []
    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)
    def del_friend(self, friend):
        if friend in self.friends:
            self.friends.remove(friend)
    def send_invites(self, msg):
        msg = self.name + ": " + msg
        for f in self.friends:
            f.update(msg)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    party = Party("Midnight Pub")
    nick = Friend("Nick")
    john = Friend("John")
    lucy = Friend("Lucy")
    chuck = Friend("Chuck")

    party.add_friend(nick)
    party.add_friend(john)
    party.add_friend(lucy)
    party.send_invites("Friday, 9:00 PM")
    party.del_friend(nick)
    party.send_invites("Saturday, 10:00 AM")
    party.add_friend(chuck)

    assert john.show_invite() == "Midnight Pub: Saturday, 10:00 AM"
    assert lucy.show_invite() == "Midnight Pub: Saturday, 10:00 AM"
    assert nick.show_invite() == "Midnight Pub: Friday, 9:00 PM"
    assert chuck.show_invite() == "No party..."
    print("Coding complete? Let's try tests!")
