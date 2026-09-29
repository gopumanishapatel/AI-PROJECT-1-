with open("AIsample.txt","r")as file:
    text = file.read()
    print(text)

chunks = []
chunk_size = 25 # 10,30, 40, 50
chunk_overlap = 10#5,15,30
step = chunk_size - chunk_overlap
for i in range(0,len(text),chunk_size):
    chunk = text[i:i+chunk_size]
    chunks.append(chunk)
print("number of chunks:",len(chunks))
for  i in range(len(chunks)):
    print(f"chunk {i} -> {chunks[i]}")
#embeddings
embeddings = model.encode(chunks)
print("Embeddings created successfully.")
print("No of embeddings",len(embeddings))