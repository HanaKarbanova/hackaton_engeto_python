from random import randint
'''open dictionary'''
dictionary = open('words.txt','r')
'''make list from dictionary'''
dic = list(dictionary)
'''how long is dictionary'''
l=len(dic)
'''random number in interval from 1 to how to long dictionary'''
number= randint(1,l)
'''select word on random position'''
word = list(dic[number].strip())
'''make tuple from word'''
word_tuple=[]
for i in word:
    word_tuple.append((i,0))
'''how long player can guess'''
repeat=len(word)
'''gues word'''
print('We guess word about',repeat, 'letters')
letter = input("Guess letter:")
while repeat >=1:
    if letter in word:
        l=0
        for i in word_tuple:
            if letter==i[0] and i[1]==0:
                word_tuple[l]=(i[0],1)
                answer="You guest"
            elif letter==i[0] and i[1]==1:
                answer='This letter is guessed!'
            if word_tuple[l]==(i[0],1):
                print(i[0],end="")
            else:
                print('_',end="")
            l+=1
        print()
        print(answer)
    else:
        print("You didn't guess!")
    letter=input('Guess again:')
    repeat-=1

print('You fail!')
