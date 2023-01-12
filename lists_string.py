my_list = []

my_list.append("Adam")

my_list.append("Sultan")

my_list.reverse()

my_list.clear()

my_list.append("Adam")

my_list.append("Sultan")

count = my_list.count("Adam")

element = my_list.pop()

my_list.append("Sultan")
my_list.append("Adem")
my_list.append("Saad")

# VI kan inte jämföra stränger med siffror så det måste vara samma datatyp i listan
# my_list.append(1)
# my_list.append(True)

my_list.sort(reverse=True)

# print(my_list, count, element)

list2 = [1, 10, 43, 4, True, False]

list2.sort()

# print(list2)

my_string = "Hej, jag heter Adam"
# print(my_string)
my_string_list = list(my_string)
# print(my_string_list)

my_split_string = my_string.split('H')
# print(my_split_string)

my_email = "adam@mujina.se"

# Denna är samma som nedan
my_domain = my_email.split('@')[1]#.split('.')[0]
# print(my_domain)

# split_sring = my_email.split('@')
# print(split_sring)
# domain = split_sring[1]
# print(domain)
# split_domain = domain.split('.')
# print(split_domain)
# company = split_domain[0]
# print(company)

letter_list = ["A", "D", "A", "M"]

my_name = "".join(letter_list)
print(my_name)

my_name_again = letter_list.join()
print(my_name_again)