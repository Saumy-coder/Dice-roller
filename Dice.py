import random
response = 'y'
def roll_a_dice():
    response='y'
    print('[-----]')
    number = random.randint(1,6)
    if(number==1):
        print('[     ]')
        print('[  0  ]')
        print('[     ]')
    elif(number==2):
        print('[  0  ]')
        print('[     ]')
        print('[  0  ]')
    elif(number==3):
        print('[  0  ]')
        print('[  0  ]')
        print('[  0  ]')
    elif(number==4):
        print('[ 0 0 ]')
        print('[     ]')
        print('[ 0 0 ]')
    elif(number==5):
        print('[ 0 0 ]')
        print('[  0  ]')
        print('[ 0 0 ]')
    elif(number==6):
        print('[0 0 0]')
        print('[     ]')
        print('[0 0 0]')
    print('[-----]')
    
    resp = input("Press y to roll again and n to exit ")

    if(resp=='y'):
        roll_a_dice()
    if(resp=='n'):
        exit


roll_a_dice()
