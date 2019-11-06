class Enemy:
    life = 3

    def attack(self):
        print("ouch")
        self.life = 1
    def checklife(self):
        if self.life <= 0:
            print("I am dead\n")
        else:
            print( self.life , " life left\n")
enemy1 = Enemy()
enemy1.attack()
enemy1.checklife()