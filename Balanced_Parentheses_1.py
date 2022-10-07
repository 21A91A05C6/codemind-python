def paraCheck(seq):
   while 1:  
       if '()' in seq :  
           seq = seq.replace ( '()' , '' )  
       elif '{}' in seq :  
           seq = seq.replace ( '{}' , '' )  
       elif '[]' in seq :  
           seq = seq.replace ( '[]' , '' )  
       else :  
           return not seq 
   
s=input()
print(paraCheck(s))