import string
import random


if __name__=="__main__":
    s1=string.ascii_lowercase
    s2=string.ascii_uppercase
    s3=string.digits          
    s4=string.punctuation
    s4
    l=int(input("Enter Password Length\n"))
    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    
    random.shuffle(s)
    print("Your Password is ready")
    print("".join(s[0:l]))
    #another technique to generate random strings out of given list
    #print("".join(random.sample(s,l)))
    
    
    
