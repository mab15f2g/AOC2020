password_list = []

with open ("passwords") as file:
    password_list = file.read().splitlines()


counter = 0
counter2 = 0


##############
# Part One
##############

for a in password_list:
    # val and pwd split
    con_pwd = a.split(": ")
    # set pwd
    pwd = con_pwd[1]

    # val splitting
    val = con_pwd[0].split(" ")
    char = val[1]

    #min max split
    min_max = val[0].split("-")
    min_value , max_value =  int(min_max[0]),  int(min_max[1])


    char_count = pwd.count(char)

    if char_count >= min_value and char_count <= max_value:
        counter += 1


print(counter)

##############
# Part Two
##############

for a in password_list:
    # val and pwd split
    con_pwd = a.split(": ")
    # set pwd
    pwd = con_pwd[1]

    # val splitting
    val = con_pwd[0].split(" ")
    char = val[1]

    #min max split
    min_max = val[0].split("-")
    min_value , max_value =  int(min_max[0]),  int(min_max[1])


    char_count = pwd.count(char)

    if (pwd[min_value -1] == char) ^ (pwd[max_value -1] == char):
        counter2 += 1        
print(counter2)

   
    
    

