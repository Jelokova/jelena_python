
# Age calculation
current_year = 2022
year_of_birth = 1988
age =current_year - year_of_birth
print(age)

# calcualation of code 2
code_1 = 354
code_3 = 132
code_2_calcul = (((code_1 / code_3) - (code_1 // code_3))*13)**0.5 #match calculation for code 2
    #print (code_2_calcul)
code_2 = int(float(code_2_calcul))
print ("Missing code_2 = " + str(code_2))

# print full secret code
my_code = (str(int(code_1)), str(int(code_2)),str(int(code_3)))
secret_code = "-".join(my_code)
print (secret_code)

# print full sting
user_name = 'John'
user_surname = 'Smith'
age=str(int(age))
print ("Hello " +user_name,"" +user_surname, ". You are " +age, "years old. Your secret code is " +secret_code,".")

#Mary Gold. You are 26 years old. Your secret code is 475-12-967.)