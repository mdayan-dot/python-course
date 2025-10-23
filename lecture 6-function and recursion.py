#functions is said to a block if codes which makes our task easier by making us not using the same block
#of codes repeatedly instead of that we can use functions

# def calc_sum(a,b):
 #   sum=a+b
  #  print(sum)
   # return sum
#in this function , def calc_sum(a,b):, is function defination
   #(a,b) are parameters
#calc_sum(5,2), is a function call
    

def calc_sum(a,b):
    sum=a+b
    print(sum)
    return sum

calc_sum(5,2)




#WAF to print the lenght of a list
def list_size(list):
    print(len(list))
    return len


no=[2,3,4,5,6,7]

list_size(no)


ayan=["chill","rude","toxic"]

list_size(ayan)


#WAF to print the elements of a list in a single line

def all_list(list):
    for item in list:
        print(item,end=" ")


all_list(ayan)        


#WAF to find the factorial of n.

def fact(n):
    fact=1
    for i in range(1,n+1):
        fact *=i
        print(fact)

fact(8)        
    


#WAF to convert USD into INR
def convt(usd):
    inr_val=usd*83
    print(usd,"USD=", inr_val,"INR")

convt(9)

# recursive function is a type of function which call itself
# for having a stop at its calling we use a base case
# example for recursive function

def show(n):
    if (n== -1):
     return
    print(n)
    show(n-1)

show(9)



#write a recursive function to print all the elements of the list

def print_list(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

print_list(ayan)


