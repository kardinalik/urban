def all_variants(text):
    for size in range(len(text)):
        for x in range(len(text) - size):
            yield text[x:x+size+1]

a = all_variants("abc")
for i in a:
    print(i)
