a=float(input('a='))
d='*'
c='+'
e='-'
f='/'
g='&'
h='^'
print(d,"ko'paytirish")
print(c,"qo'shish")
print(e,"ayirish")
print(f,"bo'lish")
print(g,'ildiz chiqarish')
print(h,"darajaga ko'tarish")
print('birortasini tanlang')
amal=input('amal=')
if amal==d:
    b=float(input('b='))
    k=a*b
elif amal==c:
    b=float(input('b='))
    k=a+b
elif amal==e:
    b=float(input('b='))
    k=a-b
elif amal==f:
    b=float(input('b='))
    k=a/b
elif amal=='&':
    k=a**(1/2)
elif amal==h:
    b=float(input('daraja b='))
    k=a**b
else:
    k="to'g'ri amal kiriting"
    d='*'
    c='+'
    e='-'
    f='/'
    g='&'
    h='^'
    print(d,"ko'paytirish")
    print(c,"qo'shish")
    print(e,"ayirish")
    print(f,"bo'lish")
    print(g,'ildiz chiqarish')
    print(h,"darajaga ko'tarish")
    print('iltimos birortasini tanlang')
    amal=input('amal=')
    if amal==d:
        b=float(input('b='))
        k=a*b
    elif amal==c:
        b=float(input('b='))
        k=a+b
    elif amal==e:
        b=float(input('b='))
        k=a-b
    elif amal==f:
        b=float(input('b='))
        k=a/b
    elif amal=='&':
        k=a**(1/2)
    elif amal==h:
        b=float(input('daraja b='))
        k=a**b
    else:
        k='imkoniyat 0 ga teng'
print(k)

