# bitch caller
bitch=True

while bitch==True:
    ask=input('\n>> Would you like to be insulted?\n')
    
    if ask.upper()=='YES' or ask.upper()=='Y' or ask.upper()=='PLEASE' or ask.upper()=='YA' or ask.upper()=='OK' or ask.upper()=='YEAH':
        print('\n>> YOU\'RE A BITCH!!\n')
    
    elif ask.upper()=='NO' or ask.upper()=='N' or ask.upper()=='NAH' or ask.upper()=='STOP':
        bitch=False
        print('\n>> Understood, have a nice day.\n')
    
    elif ask.upper()=='I LOVE YOU':
        print('\n>> I love you too.\n')     
        
    else:
        print('\n>> Input not understood, bitch. Try again.\n')
