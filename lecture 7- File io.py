
#create a new file "practie.txt" and write any text in it.

with open("practice.txt","w") as f:
    f.write("hello too brother\nlove you too")



#WAF to replace the of occurance of too with to in above file.
    


with open("practice.txt","r") as f:
     data=f.read()
new_data= data.replace("too","to")
print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)

#search that the word love is available in the file or not

with open("practice.txt","r") as f:
     data=f.read()
     
     if(data.find("love") != -1):
         print("found")
     else:
         print("not there")
