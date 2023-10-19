#ex1
def factorial(n):
  if(n==0):
    return 1
  else:
    count=1
    fact=""
    for i in range(1,n+1):
      count*=i
      fact+=str(i)
      if i!=n:
        fact+="*"
    return str(count)+"("+str(fact)+")"
  
i=int(input('enter an integer '))
result=factorial(i)
print(result)

#ex2
def div(n):
  if n ==0:
    return []
  else:
    fact=[]
    for i in range(1,n+1):
      if n%i==0:
        fact.append(i)
  
    return fact
      
  
x=int(input('enter to find divisors:'))
divisors=div(x)
print(divisors)

#ex3
def reverse(s):
  new_s=""
  for i in range(len(s)-1,-1,-1):
    new_s+=s[i]

  return new_s

s="oneword"
a=reverse(s)
print(a)

#ex4
def is_even(list):
  even_nb=[]
  for i in list:
    if i%2==0:
      even_nb.append(i)
  return even_nb

hi=[1,3,5]
bye=[5,3,18,4,2,7,10]
ev=is_even(hi)
z=is_even(bye)
print(ev)
print(z)

#ex5
def strg_pass(pas):
  has_upper=False
  hase_lowwer=False
  has_digit=False
  is_special=False
  special_characters = "!@#$%^&*()_+[]{}|;:'\",.<>?`~"
  for i in pas:
    if i.isupper():
      has_upper=True
  
    elif i.islower():
      hase_lowwer=True
    elif i.isdigit():
      has_digit=True
    elif i in special_characters:
      is_special=True

  if has_digit and has_upper and hase_lowwer and is_special and len(pas)>=8:
      return "Strong password"
  else:
      return "Weak password"
    

pass1=input('enter password')
check=strg_pass(pass1)
print(check)
pass2="password"
check2=strg_pass(pass2)
print(check2)# weak pass
