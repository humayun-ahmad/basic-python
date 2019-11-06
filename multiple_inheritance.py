class Mario():
    def mov(self):
        print("I am moving")

class  shroom():
    def shroom(self):
        print("now I am big!")
class bigMario(Mario, shroom):
    pass
bm = bigMario()
bm.mov()
bm.shroom()