import math
ran = False
def run():
    print("Your List of Symbols is : \t\t\t Example ((p2q)4(1p))\n ¬[1] not\n Λ[2] and\n ν[3] or\n →[4] imp\n x[5] xor\n ↓[6] nor")
    print("")
    current_formula = input("Enter a formula using single char variables >>").strip()
    letter=""
    folen = len(current_formula)
    class WffTest(object):
        def split2(word): 
                return [char for char in word]
        @staticmethod
        def booleangen(primarray):
            thislist = []
            liarray = []
            l = 0
            for p in primarray:
                if(len(p[2])==0):
                    l = l + 1
                else:
                    pass
            x = 2**l
            for y in range(0,l):
                line = [primarray[y][0]]
                liarray.append(((str(line)).strip(']'+'[').replace(',',' |').replace('\'','')))
                if(len(primarray[y][2])==0):
                    
                    thislist.append(line)
                    truthVal = False
                    dub = 2**(l-y-1)
                    rot = (int)(math.floor(dub))
                    for z in range(0,x):
                        if((z%rot)==0):
                            truthVal = not truthVal
                        thislist[y].append(truthVal)

            def fand(x,y,thislist,primarray):
                for  m in range (1,len(thislist[0])):
                    ans = ((thislist[x-1][m]) and (thislist[y-1][m]))
                    trulist.append(ans)
                thislist.append(trulist)
                return

                
            def fuor(x,y,thislist,primarray):
                for  m in range (1,len(thislist[0])):
                     ans = ((thislist[x-1][m]) or (thislist[y-1][m]))
                     trulist.append(ans)
                thislist.append(trulist)     
                return

            def fimp(x,y,thislist,primarray):
                for  m in range (1,len(thislist[0])):
                     ans = ((not thislist[x-1][m]) or (thislist[y-1][m]))
                     trulist.append(ans)
                thislist.append(trulist)     
                return
            def fxor(x,y,thislist,primarray):
                for  m in range (1,len(thislist[0])):
                     ans = ((thislist[x-1][m])^(thislist[y-1][m]))
                     trulist.append(ans)
                thislist.append(trulist)     
                return
            def fnor(x,y,thislist,primarray):
                for  m in range (1,len(thislist[0])):
                     ans = not(((thislist[x-1][m]) or (thislist[y-1][m])))
                     trulist.append(ans)
                thislist.append(trulist)     
                return
                    
            for itera in range(l,len(primarray)):
                trulist=[]
                trulist.append(len(thislist)+1)
                liarray.append(str(len(thislist)+1))
                if(primarray[itera][0] in ('¬')):
                    select = primarray[itera][2]
                    for item in (thislist[select[0]-1][1:]):
                        trulist.append( not item)
                    thislist.append(trulist)
                elif(primarray[itera][0] in ('Λ','ν','→','x','↓')):
                    if(primarray[itera][0]==('Λ')):
                        fand((primarray[itera][2][0]),(primarray[itera][2][1]),thislist,primarray)
                    if(primarray[itera][0]==('ν')):
                        fuor((primarray[itera][2][0]),(primarray[itera][2][1]),thislist,primarray)
                    if(primarray[itera][0]==('→')):
                        fimp((primarray[itera][2][0]),(primarray[itera][2][1]),thislist,primarray)
                    if(primarray[itera][0]==('x')):
                        fxor((primarray[itera][2][0]),(primarray[itera][2][1]),thislist,primarray)
                    if(primarray[itera][0]==('↓')):
                        fnor((primarray[itera][2][0]),(primarray[itera][2][1]),thislist,primarray)
                
                
            #This part Computes to String and sets up boolean tables
            q = int(x)+1
            liarray.pop()
            added = str(liarray).strip(']'+'[').replace(',',' |').replace('\'','')+ " |"+ "\n"
            while(x>0):
                for v in range(len(primarray)-1,0,-1):
                        if(thislist[len(primarray)-1-v][q-x]==True):
                            vx = "T"
                        else:
                            vx = "F"
                        if ((len(primarray)-1-v)>=8):
                            added = added + vx +" |  "
                        else:
                            added = added + vx +" | "
                        if(v==1):
                            added = added + "\n"
                            x = x-1
                        if(x==0):
                            return(added)
        @staticmethod
        def find_replace(string):
            def split2(word): 
                return [char for char in word]
            characters = split2(string)
            symbol_array  = ['¬','Λ','ν','→','x','↓']
            list_size = []
            for x in range(1,len(symbol_array)+1):
                list_size.append(str(x))
                
                
                
            for y in range(0,len(characters)):
                if (characters[y] in list_size):
                    characters[y]=symbol_array[int(characters[y])-1]
            returned = ''.join(characters)

            return (returned)          
        @staticmethod
        def run_const(entry,letpos):
            k = letpos
            c = 0
            rarray=[] 
            sarray=[] 
            resu=[]

            def cc(string,final):
                    result = ""
                    add = ""
                    space = 2 + folen
                    dif = len(string)
        
                
                    if(len(string)<=1):
                        rarray.append(string)
                        add = " "*(space-dif)+ " is the base case variable."
                        sarray.append(add)
                    elif(((('→') in string) or (('Λ') in string) or (('ν') in string)or (('x') in string) or (('↓') in string) ) and (len(string)>4)and string[1]!="¬"):
                        cstring = string
                        for x in range((len(rarray))-1,-1,-1):
                            if (rarray[x]) in string:
                                leng = len(rarray[x])
                                pos = string.find(rarray[x])
                                p = pos+leng
                                s = string[pos:p]
                                string = string.replace(s,(str(x+1)))
                        for l in string:
                            if( l in ("Λ","→","ν","x","↓")):
                                j = string.find(l)
                                add= " "*(space-dif) + " O"+string[j]+" on " + string[1:j] + " and " + string[j+1:len(string)-1]
                                sarray.append(add)
                                rarray.append(cstring)
                    elif(("¬") in string):
                      added=False
                      for x in string:
                         if x in string and x in("¬") and string.find(x)==1 and added==False:
                            i = string.find(x)
                            v = string[i+1:len(string)-1]
                            add = " "*(space-dif)+ " O¬ on " + str(rarray.index(v)+1)
                            rarray.append("(¬"+v+")")
                            sarray.append(add)
                            added=True
                         




                    for z in range(0,len(rarray)):
                        result = result+"\n"+ str(z+1)+". "+str(rarray[z]) +" "+ str(sarray[z])# returned line by line to be compiled
                    if final==1:
                        array = []
                        array.append(result)
                        array.append(rarray)
                        array.append(sarray)
                        array.append(z+1)
                        return array
                    else:
                        return ""
            
            def search(entry, pos, sign):
              h=0
              edt=""
              if(sign in ('+')):
                for y in range (pos+1,len(entry)):
                  if( ('(') in entry[y]):
                    h = h + 1
                  elif ( (')') in entry[y]):
                    h = h - 1
                  i = h
                  if(i>=0):
                    edt = entry[(pos+1):y+1]
                  elif(i<0):
                    return edt + entry[y];
                return edt
              
              if(sign in ('-')):
                h=0
                for y in range (pos-1,-1,-1):
                  if( ('(') in entry[y]):
                    h = h - 1
                  elif ( (')') in entry[y]):
                    h = h + 1
                  i = h
                  if(i>0):
                    edt = edt + entry[(y-1):y]
                  elif(i<0):
                    edt = entry[pos-1]+edt + entry[y];
                    return edt[::-1]
            for item in k.keys():
                cc(item,0)    
            for x in range(0,len(entry)):
              if(entry[x] in ('Λ','ν','→','x','↓')):
                res = str(search(entry,x,'-')) + str(entry[x])+ str(search(entry,x,'+'))
                if res not in resu:
                    resu.append(res)
                    resu.sort(key=len)
              elif(entry[x] in ('¬')):  
                res =  '(' + entry[x] + search(entry,x,'+')
                if res not in resu:
                    resu.append(res)
                    resu.sort(key=len)
            for x in range(0,len(resu)):
                if(x!=len(resu)-1):
                    cc(resu[x],0)
                else:
                    resultant = cc(resu[x],1)
                    print(cc(resu[x],1)[0])
            return resultant            
        @staticmethod
        def setup(string):
            non_variables = ['¬','Λ','ν','→','(',')','x','↓']
            variables = []
            variables_nm = []
            def split2(word): 
                return [char for char in word]
            count = 0
            lscount = 0
            ncount = 0
            vcount = 0
            characters = split2(string)
            letpos = {}
            for x in range(0,len(characters)):
                if( ('(') in characters[x]):
                    count = count + 1
                    lscount = lscount + 1
                elif ( (')') in characters[x]):
                    count = count - 1
                if(count==0 and (x!= (len(characters)-1 or 0))):
                    raise Exception('The initial segment was incomplete: {}'.format(x)+' was the bracket count and {}'.format(characters[x])+' was encountered before the end of the formula.') 
                if (characters[x] not in non_variables):
                    vcount = vcount+1
                    if(characters[x] not in variables_nm):
                        variables_nm.append(characters[x])
                        variables.append(characters[x]+ " depth is : "+str(count))
                    else:
                        pos = variables_nm.index(characters[x])
                        edited = variables.pop(pos)                        
                        edited = edited +", " + str(count)
                        variables.insert(pos, edited)
                if (characters[x] == "¬"):
                    ncount = ncount+1
                def proven(lscount,vcount,ncount):
                    if(lscount==((vcount+ncount)-1)):
                        return True
                    else:
                        return False


            def orderArray(array):
                for x in range(0,len(data_array)):
                    if len(array) <= 1:
                        return array
                    else:
                        # Large + Pivot + Small
                        return orderArray([n for n in array[1:] if n> array[0]])+ [array[0]] + orderArray([n for n in array[1:] if n<= array[0]]) # The Smaller or equal then Pivot
            for s in variables:
                letter = s[0]
                data = (s.split(":")[1]).strip(" ")
                # turn the input data into an array
                data_array = (list)(data)
                if (" ") in data_array:
                    data_array.remove(" ")
                if (",") in data_array:
                    data_array.remove(",")
                ordered_da = orderArray(data_array)
                letpos[letter]= ordered_da
            ans = []
            ans.append((letpos))
            ans.append(count)
            ans.append(proven(lscount,vcount,ncount))
                
            return ans
            # Upon Completion of Setup /////////////////////////////////////////////////////////
            #[0] = Dict with letter position
            #[1] = The count of left and right brackets 0 = possible wff
            #[2] = Checks proven a function that checks the equation lsbrackets = variables + negations - 1 a trait of all wff. just a test will add more comparisons later on completion
            

    # Checks to make sure the inputs are actual logical values
    try:
        entry = WffTest.find_replace(current_formula)
        ans = WffTest.setup(entry)
        proven=False
        letpos = ans[0]
        count = ans[1]
        proven = ans[2]
        primarray = []
        used = []
        opar = []
        ucount = 0
        result = ""
        print("")
        print("  Contruction Sequence Of : " + entry)
        if(count==0 and proven==True):
            result = WffTest.run_const(entry,letpos)
            #result[0] = the construction sequence of the array
            #result[1] = the functions in order of length
            #result[2] = the spacing plus the operation text
            #result[3] = the number of steps in the construction sequence.
            for x in result[2]:
                a = x.strip()
                if(a in used):
                    ucount = ucount + 1
                else:
                    used.append(a)
                    
                if(a[0]==('O')):
                    if(a[1] in ('¬')):
                        sel = ((int)(a.replace("O¬ on ","")))
                        opar = [sel]

                    elif(a[1] in ('Λ')):
                        sel = a.replace("OΛ on ","")
                        opar = sel.split(' and ')
                        
                    elif(a[1] in ('ν')):
                        sel = a.replace("Oν on ","")
                        opar = sel.split(' and ')
                        
                    elif(a[1] in ('→')):
                        sel = a.replace("O→ on ","")
                        opar = sel.split(' and ')
                    elif(a[1] in ('x')):
                        sel = a.replace("Ox on ","")
                        opar = sel.split(' and ')
                    elif(a[1] in ('↓')):
                        sel = a.replace("O↓ on ","")
                        opar = sel.split(' and ')
                        
                    for i in range(0, len(opar)):
                        opar[i] = int(opar[i])
                    primarray.append([a[1],False,opar])
                    if(len(primarray)< result[3]):
                        continue
                    else:
                        primarray.append([a[1],True,opar])
                else:
                    primarray.append([result[1][ucount],False,[]])
            print("\n" + "           Truth Table of The Function    (step number below)")
            print(WffTest.booleangen(primarray))
            ran = True
            key = input(" Enter R to Restart  >>")
            if (key.lower()==("r")):
                print("_" * 99)
                print( 2*"\n")
                run()
            else:
                pass
        else:
            raise Exception('The lb / rb must be equal and wff tests should run the value of proven and count were: {}'.format(proven)+' and {}'.format(count)+' Left brackets more then Right Brackets')
        
    except Exception as e:
          print(str(e))
          key = input(" Enter R to Restart  >>")
          if (key.lower()==("r")):
              print("_" * 99)
              print( 2*"\n")
              run()
          else:
              pass
          
if (ran == False):
    print("      ___           ___           ___                                  ___           ___                   ")
    print("     /\  \         /\__\         /\__\                                /\__\         /\__\                  ")
    print("    _\:\  \       /:/ _/_       /:/ _/_                  ___         /:/ _/_       /:/ _/_         ___     ")
    print("   /\ \:\  \     /:/ /\__\     /:/ /\__\                /\__\       /:/ /\__\     /:/ /\  \       /\__\    ")
    print("  _\:\ \:\  \   /:/ /:/  /    /:/ /:/  /               /:/  /      /:/ /:/ _/_   /:/ /::\  \     /:/  /    ")
    print(" /\ \:\ \:\__\ /:/_/:/  /    /:/_/:/  /               /:/__/      /:/_/:/ /\__\ /:/_/:/\:\__\   /:/__/     ")
    print(" \:\ \:\/:/  / \:\/:/  /     \:\/:/  /               /::\  \      \:\/:/ /:/  / \:\/:/ /:/  /  /::\  \     ")
    print("  \:\ \::/  /   \::/__/       \::/__/               /:/\:\  \      \::/_/:/  /   \::/ /:/  /  /:/\:\  \    ")
    print("   \:\/:/  /     \:\  \        \:\  \               \/__\:\  \      \:\/:/  /     \/_/:/  /   \/__\:\  \   ")
    print("    \::/  /       \:\__\        \:\__\                   \:\__\      \::/  /        /:/  /         \:\__\  ")
    print("     \/__/         \/__/         \/__/                    \/__/       \/__/         \/__/           \/__/  ")
    print("\n")
    print("\t"*10 +"Done by Orion")
    print("\n")
    
    run()
key = input(" Enter R to Restart  >>")
if (key.lower()==("r")):
    run()
else:
    pass
    


