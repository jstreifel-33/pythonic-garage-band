class Band:
    instances = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.instances.append(self)

    def play_solos(self):
        solos = list(range(len(self.members)))
        for idx, member in enumerate(self.members):
            solos[idx] = member.play_solo()
        
        return solos

    @classmethod
    def to_list(cls):
        return cls.instances


class Musician:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"{type(self).__name__} instance. Name = {self.name}"
    
    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return self.solo


class Guitarist(Musician):
    instrument = "guitar"

    solo = "face melting guitar solo"

class Bassist(Musician):
    instrument = "bass"

    solo = "bom bom buh bom"


class Drummer(Musician):
    instrument = "drums"

    solo = "rattle boom crash"