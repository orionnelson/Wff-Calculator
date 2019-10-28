import random
print("Your List of Symbols is :\n ¬[1]\n Λ[2]\n ν[3]\n →[4]")
current_formula = input("Enter formula including elements :").strip()
letter=""
folen = len(current_formula)
class WffTest(object):
    def split2(word): 
            return [char for char in word]
    @staticmethod
    def find_replace(string):
        def split2(word): 
            return [char for char in word]
        characters = split2(string)
        symbol_array  = ['¬','Λ','ν','→']
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
        rarray=[] #regular
        sarray=[] #other
        resu=[]

        # cc takes the items in order of least complex to most complex and creates the construction sequence.
        def cc(string,final):
                result = ""
                add = ""
                space = 2 + folen
                dif = len(string)
    
            
                if(len(string)<=1):
                    rarray.append(string)
                    add = " "*(space-dif)+ " is the base case variable."
                    sarray.append(add)
            #(¬a) or ¬a or ¬a)
                elif((("¬") in string) and (len(string)in(2,3,4))):
                  for x in string:
                     if x in string and x not in("¬","(",")"):
                        i = string.find(x)
                        v = string[i]
                        add = " "*(space-dif)+ " O¬ on " + str(rarray.index(v)+1)
                        rarray.append("(¬"+v+")")
                        sarray.append(add)

            #(a→b) or ((¬a)→(¬b)) or ((a→b)Λ((¬a)→b)) or if you messed up a→b) tho make sure** not 
                elif((('→') in string) or (('Λ') in string) or (('ν') in string) and (len(string)>4)):
                #replace the items with their index
                    cstring = string
                    for x in range((len(rarray))-1,-1,-1):
                        if (rarray[x]) in string:
                        #print(string + " original")
                            leng = len(rarray[x])
                            pos = string.find(rarray[x])
                            p = pos+leng
                        #print(p)
                        #print(pos)
                            s = string[pos:p]
                        #print(s)
                        #print(str(x+1))
                            string = string.replace(s,(str(x+1)))
                        #print(string + " changed")
                    #print(string)
                    for l in string:
                        if( l in ("Λ","→","ν")):
                            j = string.find(l)
                            add= " "*(space-dif) + " O"+string[j]+" on " + string[1:j] + " and " + string[j+1:len(string)-1]
                            sarray.append(add)
                            rarray.append(cstring)
                for z in range(0,len(rarray)):
                    result = result+"\n"+ str(z+1)+". "+str(rarray[z]) +" "+ str(sarray[z])# returned line by line to be compiled
                if final==1:
                    return result
                else:
                    return "."
        
        def search(entry, pos, sign):
          h=0
          edt=""
          if(sign in ('+')):
            #print("called")
            for y in range (pos+1,len(entry)):
              #print((str(pos+1)) + " to "+ str(len(entry)))
              #remember to end loop early upon finding )
              if( ('(') in entry[y]):
                h = h + 1
              elif ( (')') in entry[y]):
                h = h - 1
              #print(str(h) + str(entry[y]) )
              #print(clis)
              i = h
              #print(i)
              if(i>=0):
                #print(str(pos+1) +" : "+ str(y))
                edt = entry[(pos+1):y+1]
                #print(edt)
              elif(i<0):
                #print (edt + entry[y])
                return edt + entry[y];
            #print(edt + "edt")
            #y = len(entry)-1 # should close y
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
                #print(str(pos-1) +" : "+ str(y))
                edt = edt + entry[(y-1):y]
              elif(i<0):
                edt = entry[pos-1]+edt + entry[y];
                return edt[::-1]
        for item in k.keys():
            print(cc(item,0))    
        for x in range(0,len(entry)):
          if(entry[x] in ('Λ','ν','→')):
            res = str(search(entry,x,'-')) + str(entry[x])+ str(search(entry,x,'+'))
            if res not in resu:
                resu.append(res)
                resu.sort(key=len)
          elif(entry[x] in ('¬')):  
            res =  '(' + entry[x] + search(entry,x,'+')
            if res not in resu:
                resu.append(res)
        for x in range(0,len(resu)):
            if(x!=len(resu)-1):
                print(cc(resu[x],0))
            else:
                print(cc(resu[x],1))
                
    @staticmethod
    def setup(string):
        non_variables = ['¬','Λ','ν','→','(',')']
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
            #current depth is the count we want to retrive the opening and closing brackets
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
                    #print(str(lscount)+ " != " + str(vcount+ncount-1))
                    return True
            

        # our function starts by finding the deepest part of the array array and then finding the functions at that depth


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
entry = WffTest.find_replace(current_formula)
ans = WffTest.setup(entry)
proven=False
letpos = ans[0]
#print(letpos)
#print(entry)
count = ans[1]
proven = ans[2]
result = ""
try:
    if(count==0 and proven==True):
        result = WffTest.run_const(entry,letpos)
        #print(result)
    else:
        raise Exception('The lb / rb must be equal and wff tests should run the value of proven and count were: {}'.format(proven)+' and {}'.format(count)+' Left brackets more then Right Brackets')
    
    #letpos = Dict with the letter position in the string
except Exception as e:
      print(str(e))   
        
input("hit any to exit")
    


