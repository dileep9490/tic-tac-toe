#making the postions with dictionary
box = {'topl':'','topm':'','topr':'',
        'midl':'','midm':'','midr':'',
        'lowl':'','lowm':'','lowr':''}
#printing the table
def printingtalbe():
    print('the tabel have these index values:')
    print('--------------')
    print('topl'+'|'+'topm'+'|'+'topr')
    print('--------------')
    print('midl'+'|'+'midm'+'|'+'midr')
    print('--------------')
    print('lowl'+'|'+'lowm'+'|'+'lowr')
    print('--------------')
printingtalbe()
def printbox():
    print('--------------')
    print(box['topl']+'|'+box['topm']+'|'+box['topr'])
    print('--------------')
    print(box['midl'] + '|' + box['midm'] + '|' + box['midr'])
    print('--------------')
    print(box['lowl'] + '|' + box['lowm'] + '|' + box['lowr'])
    print('--------------')
#wiriting method for taking input
for i in range(9):
    str = input('select the position: ')
    strvalue = input('enter the value at %s :'%(str))
    box[str] = strvalue
    if(i >= 4):
        #topl
        if str=='topl':
            if (strvalue == box['midl'] and strvalue == box['lowl']) or (strvalue==box['topm'] and strvalue == box['topr']):
                print('the winner is using %s'%(strvalue))
                break
        #lowl
        if str=='lowl':
            if (strvalue == box['midl'] and strvalue == box['topl']) or (strvalue==box['lowm'] and strvalue == box['lowr']):
                print('the winner is using %s'%(strvalue))
                break
        #midl
        if str=='midl':
            if (strvalue == box['topl'] and strvalue == box['lowl']) or (strvalue==box['midm'] and strvalue == box['midr']):
                print('the winner is using %s'%(strvalue))
                break
        #topm
        if str=='topm':
            if (strvalue == box['topl'] and strvalue == box['topr']) or (strvalue==box['midm'] and strvalue == box['lowm']):
                print('the winner is using %s'%(strvalue))
                break
        #lowm
        if str=='lowm':
            if (strvalue == box['topm'] and strvalue == box['midm']) or (strvalue==box['lowl'] and strvalue == box['lowr']):
                print('the winner is using %s'%(strvalue))
                break
        #topr
        if str=='topr':
            if (strvalue == box['topm'] and strvalue == box['topl']) or (strvalue==box['midr'] and strvalue == box['lowr']):
                print('the winner is using %s'%(strvalue))
                break
        #midr
        if str=='midr':
            if (strvalue == box['midm'] and strvalue == box['midl']) or (strvalue==box['topr'] and strvalue == box['lowr']):
                print('the winner is using %s'%(strvalue))
                break
        #lowr
        if str=='lowr':
            if (strvalue == box['midr'] and strvalue == box['topr']) or (strvalue==box['lowm'] and strvalue == box['lowl']):
                print('the winner is using %s'%(strvalue))
                break
        #midm
        if str=='midm':
            if (strvalue == box['midl'] and strvalue == box['midr']) or (strvalue==box['lowm'] and strvalue == box['topm'] or(strvalue==box['lowl'] and strvalue == box['topr']) or (strvalue==box['lowr'] and strvalue == box['topl'] ) ):
                print('the winner is using %s'%(strvalue))
                break


    printbox()
