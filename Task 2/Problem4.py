
pattern=input()
repeat=input()
for i in range(len(repeat)-len(pattern)):
  if repeat [i:i+len(pattern)]==pattern:
    print(i)
     
