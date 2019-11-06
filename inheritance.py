class Parents():
    def print_last_name(self):
        print('Roberts\n')

class Child(Parents):
    def Print_first_name(self):
        print('Humayun ')
    def print_last_name(self):
        print('Ahmad')

ob = Child()
ob.Print_first_name()
ob.print_last_name()