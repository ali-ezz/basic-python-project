mas=input('enter: ')
word =mas.split(' ')
empje ={
    ";)":"😉",
    ":)":"🙂",
    ":(":"🙁",
    ":|":"😐"
}
out=' '
for item in word:
   out+=empje.get(item, item) +' '
print(out)

def emoje(word):
 empje ={
    ";)":"😉",
    ":)":"🙂",
    ":(":"🙁",
    ":|":"😐"}
 out=' '
 for item in word:
   out+=empje.get(item, item) +' '
 print(out)

 
mas=input('enter: ')
word =mas.split(' ')
emoje(word)