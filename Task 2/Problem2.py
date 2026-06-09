DNA_S=input()
k=int(input())
c={}
for i in range (len(DNA_S)-k+1):

    kmer=DNA_S[i:i+k]

    if kmer in c:
        c[kmer]=c[kmer]+1
    else:
        c[kmer]=1
l=0

for kmer in c:
    if c[kmer]>l:
        l=c[kmer]

for kmer in c:
    if c[kmer]==l:
        print(kmer)
