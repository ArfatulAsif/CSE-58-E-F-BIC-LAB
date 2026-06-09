
dna = input()
complement={
    'A':'T',
    'T':'A',
    'G':'C',
    'C':'G'
}

result=""

for i in range (len(dna)):
  result+=complement[dna[i]]
print(result)
