def pal(word):
    if word==word[::-1]:
        return True
    else: 
        return False

print(pal("kayak")) 

