import random
capital = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
small   = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbol  = ['!', '@', '#', '$', '%']
number  = '0123456789'

def psd():
    for i in range(10):
    password=''
    for j in range(12):
        category = random.randint(1,4)
        if category ==1:
            password += random.choice(capital)
        elif category ==2:
            password += random.choice(small)
        elif category ===3
        else:
            password += random.choice(number)
    print(password)
