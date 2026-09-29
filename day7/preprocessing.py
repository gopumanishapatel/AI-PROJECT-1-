with open("AIsample.txt","r")as file:
    text = file.read()
    print(text)

chunks = []
chunk_size = 40
for i in range(0,len(text),chunk_size):
    chunk = text[i:i+chunk_size]
    chunks.append(chunk)
for chunk in chunks:
    print(chunk)