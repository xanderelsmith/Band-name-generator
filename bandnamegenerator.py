while (True):
    print('Welcome to a band name generator ')
    name=input('please input your town:\t')
    suffix=int(input('Alright, \n now input a value(from 1-4):\t'))
    description=['rowdy','Awesome','nawty','mystical']
    if suffix<5:
        print( description[suffix-1] +'-'+name+' rock and roll band\n\n')
    else:
        print('you inputed an option that is not specified\n\n')
    
    