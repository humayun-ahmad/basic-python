class Enemy:
    def __init__(self, x):
        self.energy = x

    def get_energy(self):
        print(self.energy)

a = Enemy(5)
sandy = Enemy(18)

a.get_energy()
sandy.get_energy()