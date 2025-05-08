# Q.1: Create a list of names and print all names using list.

# employee_name = ["yahyaraees","Abdullah","Yasir","Affan"]
# print(employee_name)


# Q.2: Create an empty list of type string called days.
# Use the add method to add names of 7 days and print all days.

# names = []
# names.append("Monday")
# names.append("Tuesday")
# names.append("Wednesday")
# names.append("Thursday")
# names.append("Friday")
# names.append("Saturday")
# names.append("Sunday")
# print(names)

# Q.3: Create a list of Days and remove one by one from the end of list.

# days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
# days.pop()
# days.pop()
# days.pop()
# days.pop()
# days.pop()
# days.pop()
# days.pop()
# print(days)



# Q.4: Create a list of numbers & write a program to get the smallest & greatest number from a list.

# list_number = [10,-1,0,-7,-4,-5]

# for num in list_number:
#     if num > 0:
#         print("Larger Number Found:", num)
#         break
# else:
#     print("No number greater than 0")

# Q5:
# Create a dictionary named contact_map with keys "name" and "phone", and store some appropriate values in it.
# Then, use a list comprehension to find all keys in the dictionary that have a length of 4 characters.
contact_map = {
   "name" : ["Yahya","Rais","siflf","kjfljdfsjfl"],
   "phone"  : ["Infinix","Mobile"],
   "nam8" : ["Yahya","Rais"],
   "phone1"  : ["Infinix","Mobile"]
}
# key_list = []
# for key in contact_map:
#     if len(key) == 4:
#      key_list.append(key)                         '''1st use ''''
#      print(key_list)   

# key_trai = [key for key in contact_map if len(key) == 5]      '''2st use '''' same work
# print(key_trai)




# Question:
# Ek dictionary ke un keys ko list mein lo jinki length 4 se zyada ho.


# sample = {"names": "yahya","father_name":"Rais uddin",}
# trai = [key for key in sample if len(key) > 4]

# print(trai)

# Question:
# Ek list banao jisme 1 se 10 tak ke sirf even numbers hon.
# range_number = [1,2,3,4,5,6,7,8,9,10]
# even_number = [key for key in range_number if key % 2 == 0]
# print(f"{even_number}even number")





# # keys_with_length_4 = [key for key in contact_map if len(key) == 4]
# print(keys_with_length_4)
 


























wordss = ["cat","dog","cow","goat"]
long_words = [key for key in wordss if len(key) > 3]
print(long_words)