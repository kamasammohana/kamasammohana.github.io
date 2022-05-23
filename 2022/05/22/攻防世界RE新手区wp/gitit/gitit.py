str = 'c61b68366edeb7bdce3c6820314b7498'
flag=''
for i in range(len(str)):
    if i & 1:
        t=1
    else:
        t=-1
    flag+=chr(ord(str[i])+t)
print(flag)
