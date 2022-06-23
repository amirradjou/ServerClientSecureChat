
import math  , random 

def toBinary(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(int(bin(i)[2:]))
  return m



def toString(a):
  l=[]
  m=""
  for i in a:
    b=0
    c=0
    k=int(math.log10(i))+1
    for j in range(k):
      b=((i%10)*(2**j))   
      i=i//10
      c=c+b
    l.append(c)
  for x in l:
    m=m+chr(x)
  return m


def nBitRandom(n):

	# Returns a random number
	# between 2**(n-1)+1 and 2**n-1'''
	return(random.randrange(2**(n-1)+1, 2**n-1))


print(nBitRandom(234))