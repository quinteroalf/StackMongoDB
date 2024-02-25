#Input : string = [ABC[23]][89]
#        index = 0
#Output : 8
#The opening bracket at index 0 corresponds
#to closing bracket at index 8.
from collections import deque


def findindex(str,pos):
    stack = []
    bcsize=i=j=0
    for i,char in  enumerate(str):
        if char=="[":    
            stack.append(char)
            size=len(stack) 
            if pos==i:
                bcsize=len(stack)        
            #print(f'O-Bracket: {char},  Stack push : {stack} index: {i} size: {size}  j: {j}\n' )
        elif char=="]": 
            size=len(stack)
            #print(f'BC-Bracket: {char},  Stack push : {stack} index: {i} size: {size}  j: {j}\n' )
            if bcsize==size:
                print(f'Resultado: {i}')
                break
            current=stack.pop()
            #print(f'C-Bracket: {char},  Stack pop  : {stack} index: {i}  size: {size}  j={j}\n')
        else:
            if pos==i:
                print("no match")
            
                

def main():
    findindex("[ABC[23]][89]", 0) # should be 8
    findindex("[ABC[23]][89]", 4) # should be 7
    findindex("[ABC[23]][89]", 9) # should be 12
    findindex("[ABC[23]][89]", 1) # No matching bracket
    findindex("[ABC[23]][89]", 3) # No matching bracket
    findindex("[[ABC[23]]][89]", 0) # No matching bracket
 
 
 
if __name__ == "__main__":
    main()
