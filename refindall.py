import re
phrase='From: csev@umich.edu to : cwen@iupui.edu about meeting @2PM  1 banana , 30 guineos, 100 platanos, 50 Aguacates, EE A message '
x=re.findall('[0-9]+',phrase) #busca uno o mas digitos
print(x)
y=re.findall('[AEIOU]+',phrase) #Busca vocales en mayuscula
print('UpperCase',y)

# matching
z=re.findall('^From.+:',phrase) # return a line that starts with from an end with :
print(z)
#non-Greedy
z=re.findall('^F.+?:',phrase) # return a line that starts with F and end with :
print(z)
#Fine-tuning
s='From stephen.marquard@uct.ac.za Sat Jan  5 09:04:16 2008'
p=re.findall('\S+@\S+',s) # search for white space at the beginning an end returning the text in the middle
l=re.findall('^From (\S+@\S+)',s) #look for line starting with from and do the same thing
print(p)
print(l)
import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
lst1=re.findall('@[0-9]+\\S+',s)
print(lst)
print(lst1)
