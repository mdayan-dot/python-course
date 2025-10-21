#WAP to store  following word meanings in a python dictioanry
#table:"a piece of furniture","list of fact and figures"
#cat:"a small animal"


dict={
    "table":["a piece of furniture","list of fact and figures"],
    "cat":"a small animal"
    }
print(dict)

#you are given a list of subjects for students . assume one classroom is required for 1 subject.how many classroom are needed for all students
#"python","java","c++","python","javascript","java","pyhton","java","c++","c"

subjects={
    "python","java","c++","python","javascript","java","python","java","c++","c"
    }
print(len(subjects))
    

#wap to enter marks of 3 subjects from the user and store them in a dictionary. start with an empty dict and add one by one

marks={}
x=int(input("enter phy:"))
marks.update({"phy":x})
x=int(input("enter chem:"))
marks.update({"chem":x})
print(marks)

#figure out a way to store 9&9.0 as seperate values in a set


value={9,"9.0"}
print(value)
