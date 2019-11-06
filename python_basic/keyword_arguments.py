def dumb_sentence(name="bucky",action="ate"):
    print(name,action)
    
dumb_sentence()
dumb_sentence("sally","farts")
dumb_sentence(action = "play")

def add_number(*args):
    total = 0
    for a in args:
        total += a
    print(total)

add_number(3)
add_number(3,32)
add_number(1,2,3,4,5)

def health_calculator(age,apples_ate,cigs_smoked):
    answer = (100-age) + (apples_ate *3.5) - (cigs_smoked*2)
    print(answer)
    
buckys_data = [27,20,0]
health_calculator(buckys_data[0],buckys_data[1],buckys_data[2])
health_calculator(*buckys_data)