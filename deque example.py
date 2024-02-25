def findindex(str,pos):
    deq = deque()
    print(str)
    i=0
    for i,char in  enumerate(str):
        if char=="[":    
            deq.append(char) 
            siz=len(deq)        
            print(f'Append Open Bracket,  Stack status : {deq} index: {i}')
        elif char=="]": 
            current=deq.pop()
            print(f'Removed Closing Bracket: {current},  Stack status:{deq} index: {i} ')
        else:
            print(f"Letter index:{i}")
            #current=stack.pop