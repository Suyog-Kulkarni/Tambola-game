import random
import time
N=input("Enter total number of player,maximum 7 players and minimum 2 players can play simultaneously: ")
if(N.isdigit()==True):
    A=[0, ]#First 0 because A[j] is going out of range.
    if(int(N)<=7 and int(N)>=2):
        for i in range(1,int(N)+1):
            for j in range(1,int(N)+1):
                a=input(f"\nEnter the {j} player name: ")
                if(a=='' or a==' '):
                    print('\nThe name should not be blank.')
                    print('\nWARNING!!,now you have only one chance.')
                    a=input(f"\nEnter the {j} player name: ")
                    if(a=='' or a==' '):
                        print('\nThe name should not be blank now it has been removed.')
                    else:
                        A.append(a)
                else:
                    A.append(a)     
            break
        A.pop(0)
        b=[ ]
        c=[ ]
        d=[ ]
        b1=[ ]
        b2=[ ]

 
        for i in A:
            def fun():
                global i
                if(A.count(i)==1):
                    #print(A.count('g'))
                    for i in A:
                        A.insert(0,0)
                        for j in range(1,len(A)):
                            print(f"\nThe name of the {j} player is\n",A[j])
                        break
                    B=input("\nEnter the name of the Host: ")
                    #B.upper()
                    if(B in A):
                        class suyog:
                            for r in range(1):
                                x = range(1, 7)
                                kl = range(64, 71)
                                ab = range(8, 15)
                                mn = range(71, 79)
                                bc = range(15, 22)
                                no = range(79, 85)
                                cd = range(22, 29)
                                op = range(85, 90)
                                de = range(29, 36)
                                qr = range(90, 95)
                                ef = range(36, 43)
                                st = range(95, 100)
                                fg = range(43, 50)
                                gh = range(50, 57)
                                ij = range(57, 64)
                            y = [x, ab, bc, cd, de, ef, fg, gh, ij, kl, mn, no, op, qr, st]
                            for l in y:
                                b.append(random.choice(l))
                            print('\n')
                            print(f'{B},Setting a list of Numbers for you...\n')
                            #time.sleep(3)
                            print(f'{B},Your 15 numbers are:- ', b)
                            A.pop(A.index(B))
                            
                            
                        e = suyog()
                        A.pop(0)
                        for n in A:
                            for j in range(len(A)):
                                s = A[j]
                                #print(A[j+1])
                                class s:
                                    #c=[ ]
                                    for k in range(1,16):
                                        x=range(1,100)
                                        random.choice(x)
                                        c.append(random.choice(x))
                                      
                                    print('\n')
                                    print(f'{s},Setting a list of Numbers for you.....\n')
                                    #time.sleep(3)
                                    print(f'{s},Your 15 numbers are:-',c)
                                   

                                    for w in c:
                                        if(c.count(w)>=2):
                                            c.remove(w)
                                            print('\n')
                                            print('Searching for repeated numbers...')
                                            #time.sleep(3)
                                            print('\n')
                                            print(f"\n{s},The number {w} in your list is repeated so it has been removed.")
                                            for i in range(500):
                                                if(len(c)<15):
                                                    O=input("\nEnter any number you want to add in your list(greater than 0 and lesser than 100) : ")
                                                    if(O.isdigit()==True and int(O)!=0 and int(O)<100):
                                                        c.append(int(O))
                                                        print(f'\n{s},Your new 15 numbers list is:- ',c)
                                                        #time.sleep(2)

                                                    elif(O.isalpha()==True):
                                                        print('\nPlease enter only numbers.')

                                                    elif(O.isdigit()==False):
                                                        print(f'\n{O} is invalid!!')
                                                    
                                                    elif(int(O)==0):
                                                        print('\n0 is invalid!!,Please only enter numbers Except 0.')

                                                    elif(int(O)>=100):
                                                        print(f'\n{O} is invalid!!,Please only enter numbers lesser than 100.')
                                                    else:
                                                        pass 
                                                    

                                                else:
                                                   pass

                                        else:
                                            pass
        
                                    if(len(A)>=2):
                                        for k in range(1,16):
                                            x=range(1,100)
                                            random.choice(x)
                                            d.append(random.choice(x))
                                      
                                        print('\n')
                                        print(f'{A[j+1]},Setting a list of Numbers for you.....\n')
                                        #time.sleep(3)
                                        print(f'{A[j+1]},Your 15 numbers are:- ',d)
                                   

                                        for w in d:
                                            if(d.count(w)>=2):
                                                d.remove(w)
                                                print('\n')
                                                print('Searching for repeated numbers...')
                                                #time.sleep(3)
                                                print('\n')
                                                print(f"\n{A[j+1]},The number {w} in your list is repeated so it has been removed.")
                                                for i in range(500):
                                                    if(len(d)<15):
                                                        O=input("\nEnter any number you want to add in your list(greater than 0 and lesser than 100) : ")
                                                        if(O.isdigit()==True and int(O)!=0 and int(O)<100):
                                                            d.append(int(O))
                                                            print(f'\n{A[j+1]},Your new 15 numbers list is:- ', d)
                                                            #time.sleep(2)
                                                    
                                                        elif(O.isdigit()==True and int(O)==0):
                                                            print('\n0 is invalid!!,Please only enter numbers Except 0.')

                                                        else:
                                                            print(f'\n{O} is invalid!!,Please only enter numbers lesser than 100.')
                                                       
                                                    

                                                    else:
                                                        pass

                                            else:
                                                pass
        

                                        
                                    else:
                                        pass


                                    if(len(A)>=3):
                                        for k in range(1,16):
                                            x=range(1,100)
                                            random.choice(x)
                                            b1.append(random.choice(x))
    
                                        for r in range(1):
                                            x=range(1,7)
                                            kl=range(64,71)
                                            ab=range(8,15)
                                            mn=range(71,79)
                                            bc=range(15,22)
                                            no=range(79,85)
                                            cd=range(22,29)
                                            op=range(85,90)
                                            de=range(29,36)
                                            qr=range(90,95)
                                            ef=range(36,43)
                                            st=range(95,100)
                                            fg=range(43,50)
                                            gh=range(50,57)
                                            ij=range(57,64)
                                
                                        yo=[x,ab,bc,cd,de,ef,fg,gh,ij,kl,mn,no,op,qr,st]
                                        for lp in yo:
                                            b1.append(random.choice(lp))
                                        print('\n')
                                        print(f'{A[j+2]},Setting a list of Numbers for you...')
                                        for i in b1:
                                            if(b1.count(i)==1):
                                                b2.append(i)
                                                if(len(b2)>14):
                                                  break
                                                else:
                                                    pass
                                            else:
                                                pass

                                        print(f'\n{A[j+2]},Your 15 numbers are:- ',b2)

                                    else:
                                        pass
                                                        
                                j=s()   
                                break                   
                                #j=s()
                            break
                        print('\n')
                        print(B,'Your list of Number is:- ',b)
                        print(A[0],'Your list of Number is:- ',c)
                        #print(A[1],'Your list of Number is:- ',b2)

                        try:
                            print(f'{A[1]} Your list of Number is:- ',d)
                            print(f'{A[2]} Your list of Number is:- ',b2)
                            
                        except IndexError:
                            pass


                        z=range(1,100)
                        print("\nThe first Number is 0,Please ignore it.")
                        for i in range(10000):
                            a=random.choice(z)
                            inpu=input("\nPlease press 0 to get the another number: ")
                            if(inpu.isdigit()==True and int(inpu)==0):
                                print("\nThe Next Number is: ",a)
                                if(a in b and a in c and a in d and a in b2):
                                    print('\n')
                                    print(f'{B},{A[0]},{A[1]} and {A[2]} you all got the Number {a}.')
                                    b.remove(a)
                                    c.remove(a)
                                    d.remove(a)
                                    b2.remove(a)
                                    print('\n')
                                    print(f'{B},Now the remaining numbers are:- ',b)
                                    print(f'\n{A[0]},Now the remaining numbers are:- ',c)
                                    print(f'\n{A[1]},Now the remaining numbers are:- ',d)
                                    print(f'\n{A[2]},Now the remaining numbers are:- ',b2)
                                    if(len(b)==0 and len(c)==0 and len(d)==0 and len(b2)==0):
                                        print(f"HURRAY!! {B},{A[0]},{A[1]} and {A[2]} you All wins!!!")

                                    else:
                                        pass

                                elif(a in b and a in c):
                                    print(f'\n{B} and {A[0]} you both got the number {a}.')
                                    b.remove(a)
                                    c.remove(a)
                                    print(f'\n{B},Now the remaining numbers are:- ',b)
                                    print(f'\n{A[0]},Now the remaining numbers are:- ',c)
                                    if(len(b)==0 and len(c)==0):
                                        print(f'\nHURRAY!!,{B} and {A[0]} you both wins.')
                                        break
                                    else:
                                        pass

                                elif(a in b and a in d):
                                    print(f'\n{B} and {A[1]} you both got the number {a}.')
                                    b.remove(a)
                                    d.remove(a)
                                    print(f'\n{B},Now the remaining numbers are:- ',b)
                                    print(f'\n{A[1]},Now the remaining numbers are:- ',d)
                                    if(len(b)==0 and len(d)==0):
                                        print(f'\nHURRAY!!,{B} and {A[1]} you both wins.')
                                        break
                                    else:
                                        pass

                                elif(a in c and a in d):
                                    print(f'\n{A[0]} and {A[1]} you both got the number {a}.')
                                    d.remove(a)
                                    c.remove(a)
                                    print(f'\n{A[0]},Now the remaining numbers are:- ',c)
                                    print(f'\n{A[1]},Now the remaining numbers are:-',d)
                                    if(len(c)==0 and len(d)==0):
                                        print(f'\nHURRAY!!,{A[0]} and {A[1]} you both wins.')
                                        break
                                    else:
                                        pass
                                elif(a in b2 and a in b and a in c):
                                    print(f'\n{A[0]},{B} and {A[2]} you three got the number {a}.')
                                    b.remove(a)
                                    c.remove(a)
                                    b2.remove(a)
                                    print(f'\n{A[0]},Now the remaining numbers are:- ',c)
                                    print(f'\n{B},Now the remaining numbers are:-',b)
                                    print(f'\n{A[2]},Now the remaining numbers are:-',b2)
                                    if(len(b2)==0 and len(b)==0 and len(c)==0):
                                        print(f'\nHURRAY!!,{A[0]},{B} and {A[2]} you three wins.')
                                        break
                                    else:
                                        pass


                                
                                    
                                elif(a in b or a in c or a in d or a in b2):
                                    if(a in b):
                                        print('\n')
                                        print(f'{B} You got the Number {a}.')
                                        b.remove(a)
                                        print('\n')
                                        print(f'{B},Now the remaining numbers are:- ',b)
                                        if(len(b)==0):
                                            print(f"\nHURRAY!!,{B} wins!!!")
                                            break
                                            

                                        else:
                                            pass
                                    
                                    elif(a in c):
                                        print('\n')
                                        print(f'{A[0]} You got the Number {a}.')
                                        c.remove(a)
                                        print('\n')
                                        print(f'{A[0]},Now the remaining numbers are:- ',c)
                                        if(len(c)==0):
                                           print(f"\nHURRAY!!,{A[0]} wins!!!")
                                           break
                            

                                        else:
                                            pass
                                    
                                    elif(a in d):
                                        print('\n')
                                        print(f'{A[1]} You got the Number {a}.')
                                        d.remove(a)
                                        print('\n')
                                        print(f'{A[1]},Now the remaining numbers are:- ',d)
                                        if(len(d)==0):
                                           print(f"\nHURRAY!!,{A[1]} wins!!!")
                                           break
                            

                                        else:
                                            pass

                                    elif(a in b2):
                                        print('\n')
                                        print(f'{A[2]} You got the Number {a}.')
                                        b2.remove(a)
                                        print('\n')
                                        print(f'{A[2]},Now the remaining numbers are:- ',b2)
                                        if(len(b2)==0):
                                           print(f"\nHURRAY!!,{A[2]} wins!!!")
                                           break
                            

                                        else:
                                            pass
                                    
                                


                                    
                                else:
                                    print('\n')
                                    #time.sleep(2)
                                    print(a,"is not present in any of the list.")
                                    #time.sleep(3)
                                    print(f'\n{B},The remaining numbers are:- ',b)
                                    #time.sleep(1)
                                    print(f'\n{A[0]},Now the remaining numbers are:- ',c)
                                    #time.sleep(1)
                                    try:
                                        print(f'\n{A[1]},Now the remaining numbers are:- ',d)
                                        print(f'\n{A[2]},Now the remaining numbers are:- ',b2)
                                    except:
                                        pass

                            else:
                                print("Please Enter 0.")
                                print(inpu,"is invalid!!")
            


                                
                            
                                
                            

                
                    else:
                        print("Their is No player having name: ",B)
                        print('Please enter the correct Host name')
            
                else:
                    print('Name should not be repeated.')
            fun()
            
            
            break
    
    else:
        print('Maximum 7 players and Minimum 2 players can play simultaneously')                 
        

else:
    print("Invalid input,please enter numbers only.")

