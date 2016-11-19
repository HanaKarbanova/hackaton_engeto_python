dictionary = open('words.txt','r')
word = 'elvis'
word_sort=''.join(sorted(word))

l = len(word)
seznam=[]

for line in dictionary:
    if l == len(line.strip()):
        seznam.append((line.strip(),''.join(sorted(line.strip()))))

anagram=[]
for i in seznam:
    if word_sort == i[1] and word != i[0]:
        anagram.append(i[0])
print(anagram)
