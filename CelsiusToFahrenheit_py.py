
# coding: utf-8

# In[ ]:


#Define Conversion function

def Convert_Function(Degree=None, Degree_Value=None):
    if Degree=="F":
        DV=((Degree_Value-32)*(5/9))
        return 'C',round(DV,2)
    elif Degree=="C":
        DV=((Degree_Value*(9/5))+32)
        return 'F',round(DV,2)
    else:
        print("Choose F or C properly !")

#First Program

print("Program to convert Celsius to farenheit and viceversa")

#Take scale input unit from user 

Degree = input("Choose F or C ? ")

#Ask user to enter the degree value

Degree_Value = float(input("Enter the temperature value : "))

#Pass the inputs to the conversion function 

d,v=Convert_Function(Degree, Degree_Value)

#Print the result after conversion

print(Degree_Value, "degrees", Degree, "is equal to", v, "degrees", d)

