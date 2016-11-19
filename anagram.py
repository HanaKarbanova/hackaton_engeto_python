dictionary = open('words.txt','r')
word = 'lost'
word_sort=''.join(sorted(word))
l = len(word)
seznam=[]
for line in dictionary:
    s=line.strip()
    if l == len(s):
        if word_sort == ''.join(sorted(s)) and word !=s:
            seznam.append(s)
print(seznam)
