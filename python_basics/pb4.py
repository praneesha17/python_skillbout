file=open("sam.txt","r")
con=file.read()
words=con.split()
print(len(words))