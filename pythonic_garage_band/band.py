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
    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"
    
    def get_instrument(self):
        return self.instrument


class Guitarist(Musician):
    instrument = "guitar"

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    def play_solo(self):
        return "face melting guitar solo"

class Bassist(Musician):
    instrument = "bass"

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    def play_solo(self):
        return "bom bom buh bom"


class Drummer(Musician):
    instrument = "drums"

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    def play_solo(self):
        return "rattle boom crash"