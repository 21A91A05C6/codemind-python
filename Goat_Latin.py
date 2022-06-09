def toGoatLatin(S):
      s = S.split(" ")
      c= 1
      a = []
      vowel = {"a","e","i","o","u"}
      for i in s:
         if i[0].lower() in vowel:
            x = i + "ma" + ("a"*c)
         else:
            x=i[1:]+i[0] + "ma" +("a"*c)
         c+=1
         a.append(x)
      return " ".join(c for c in a)
s=input()
print(toGoatLatin(s))