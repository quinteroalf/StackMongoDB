def reverse(str):
    st=[]
    reverse=""
    for char in str:
        st.append(char)
    
    while len(st)>0:
        reverse=reverse+st.pop()
    return reverse;


name="andrea"
print(reverse(name))