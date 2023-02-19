name = input('Enter file:')
try:
    handle = open(name)
except:
    name = input('Enter file that EXISTED !!!! :')



counts = {}
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print( sorted( [ (v,k) for k,v in counts.items() ], reverse=False ) )

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
print(dir(bigword))