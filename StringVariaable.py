""""
this program ask for a word and tells you the letter that is in the second position . 
it also tells you the lenght of the  word
word=input("Enter Word : ")
print(word[1])
print("tamano de la palabra", len(word))
"""
#this pogram asks for a word an use a loop to tell you the position and the letter of the word

"""
word=input("Enter word : ")

for i in range(0,len(word)):
    print("position",i, " leter : ",word[i])
"""
#Similar to the previous program ,but using the while loop
""""
i=0
word=input("enter word : ")
while(i<len(word)):
    print("the position is : ",i,"The letter is : ",word[i])
    i+=1
"""
#search letter coincidence in a word
""""

count=0
word=input("enter word:")
letter=input("letter to search in the word: ")
for i in range(len(word)):
    if word[i]==letter:
        count+=1
print("the letter",letter," appeared ",count," in the word",word)

"""""

#Check if the setence is a palindromo. 
#Ej: Anita lava la tina ---> al reves es anita lava la tina
#anita
def CheckSentence(sentence):
    EsPalindromo=None
    Pal=""
    PalInv=""
    sentenceIn=""
   
    for i in range (len(sentence)):
     if sentence[i].isspace() == False  :
        Pal+=sentence[i] 

    print(Pal)

    for x in range(len(sentence)-1,-1,-1):
       if sentence[x].isspace() == False  :
        PalInv+=sentence[x]
    print(PalInv)



 
    if  Pal==PalInv:
     EsPalindromo=True  
    
      
   
     
    return EsPalindromo

sentence = str(input("Sentence :"))

print("La oración es un palindromo: ",CheckSentence(sentence))


