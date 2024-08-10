count=0
i=0
s='XII'
while i<=len(s):
      if 'CM' in s:
         count+=900
         s=s.replace("CM","")
      elif 'IV' in s:
         count+=4
         s=s.replace("IV","")
      elif 'IX' in s:
         count+=9
         s=s.replace("IX","")
      elif 'XL' in s:
         count+=40
         s=s.replace("XL","")
      elif 'XC' in s:
         count+=90
         s=s.replace("XC","")
      elif 'CD' in s:
         count+=400
         s=s.replace("CD","")
      i+=1
for item in s:
       if item =='I':
                count+=1
       elif item =='V':
                count+=5
       elif item =='X':
                count+=10
       elif item =='L':
                count+=50
       elif item =='C':
                count+=100
       elif item =='D':
                count+=500
       elif item =='CM':
                 count+=400
       elif item =='M':
                count+=1000
print(count)