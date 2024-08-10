
num =str(input('phone: '))
for item in num:
    if item=='1':
        print('one')
    elif item=='2':
        print('two')
    elif item=='3':
        print('three')
    elif item=='4':
        print('four')
    elif item=='5':
        print('five')
    elif item=='6':
        print('six')
    elif item=='7':
        print('seven')
    elif item=='8':
        print('ehgt')
    elif item=='9':
        print('nune')
    elif item=='0':
        print('zero')
    else:
        print('that numt a number\n')
    #or
num =input('phone: ')
diget_dic = {
    "0":"zero",
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine"
}
num_ch=' '
for item in num:
 num_ch=num_ch+diget_dic.get(item,"!")+' '
print(num_ch)

    