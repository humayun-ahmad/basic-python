class Girl:
    gender = 'female'

    def __init__(self,name):
        self.name = name

f = Girl('girland')
s = Girl('tuna')
print(f.gender)
print(s.gender)
print(s.name)