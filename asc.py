#encoding=utf-8
def to2(a):
    z = []
    for i in a:
        b = ord (i)
        z.append(b)
    for k in z:
        c = bin(k)
        str(c)
        x = []
        for n in c:
            x.append(n)
        x = x[2:]
        print (x)


import math
def to10 (b) :
    w = []
    for i in b:
        q = [] 
        z = 0
        for c in i:
            int (c)
            q.append(c)
        q.reverse()
        for a in range(0, len(q)):
            num = int(q[a])
            z += num*(math.pow(2,a))
        z = int(z)
        e = chr(z)
        w.append(e)
    print w

print "Hello! What is your name?"
name = raw_input('> ')
print "Hello, %s! I'm a program that can translate" % name ,
print "any worlds into binary or numbers into worlds according to ASCII." 

while True:
    print "Please type 'YES' if you want to run me. Or 'NO' to quit me."
    c = raw_input('> ')
    if c == "YES" or c == "yes":
        print "Please choose from:"
        print """
                      1:\t(from context to 2)
                      2:\t(from contex to 10)
                      3:\t(from 2 to context)
                      4:\t(from 10 to context)
                      quit: to end me
         """
        d = raw_input("> ")
        if d == "1":
            print "Please input the context that you want to translate, and you will get the binary code of the context you put:"
            a = raw_input('> ')
            to2 (a)
            
        elif d== "2":
            w=[]
            print "Please input the context that you want to translate, and you will get the binary code of the context you put:"
            a = raw_input('> ')
            for i in a:
                i=ord(i)
                w.append(i)
            print w
        
        elif d== "3":
            print "Please input the number that you want to translate, and you will get the context you put:"
            e = raw_input('> ').split(' ')
            to10(e)

        elif d=="4":
            r=[]
            print "Please input the number that you want to translate, and you will get the context you put:"
            j = raw_input('> ').split(' ')
            for i in j:
                k = int(i)
                k = chr(k)
                r.append(k)
            print r
        elif d == "quit":
            break
            exit()
         
        else:
            print "WRONG! You have to choose the program you wan to run from the table above."
    elif c == "NO" or c == "no":
        print "Ok. Goodbye %s! It's my please to meet you!" % name
        break
        exit()

    else:
        print "Sorry, I don't understand. Please try again"
