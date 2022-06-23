import math  , random 


def toBinary(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(int(bin(i)[2:]))
  return m


def convert(list):
	
	s = [str(i) for i in list]
	res = int("".join(s))
	return(res)


def nBitRandom(n):
	return(random.randrange(2**(n-1)+1, 2**n-1))

def encrypt(me):
    en = math.pow(me,e)
    c = en % n
    print("Encrypted Message is: ", c)
    return c



message = convert(toBinary(input("Enter txt :")))

p = nBitRandom(151)
print(p)
q = nBitRandom(103)
print(q)
e = 3
 
n = p * q 
print(n)

 
print("Original Message is: ", message)
c = encrypt(message)