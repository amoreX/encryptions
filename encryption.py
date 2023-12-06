stri=input("Enter string:")
dec=input("encode or decode?")
def encode(s):
    s=list(s)
    n=len(s)
    st=""
    for i in s:
        val=ord(i)+n
        st=st+chr(val)
    return st
def decode(s):
    s=list(s)
    n=len(s)
    st=""
    for i in s:
        val=ord(i)-n
        st=st+chr(val)
    return st
if dec=="encode":
    print(encode(stri))
else:
    print(decode(stri))
