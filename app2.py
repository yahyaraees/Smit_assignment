# Q.1: Create a list of names and print all names using list.

# employee_name = ["yahyaraees","Abdullah","Yasir","Affan"]
# print(employee_name)

  # ///////////////////////////////////

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

    # ///////////////////////////////////

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

                 # ///////////////////////////////////

# Q.4: Create a list of numbers & write a program to get the smallest & greatest number from a list.

# list_number = [10,-1,0,-7,-4,-5]

# # for num in list_number:
# if list_number > 0:
#         print("Larger Number Found:",list_number)
    
# else:
#     print("No number greater than 0")

               # ///////////////////////////////////


# Q5:
# Create a dictionary named contact_map with keys "name" and "phone", and store some appropriate values in it.
# Then, use a list comprehension to find all keys in the dictionary that have a length of 4 characters.

# contact_map = {
#    "name" : ["Yahya","Rais","siflf","kjfljdfsjfl"],
#    "phone"  : ["Infinix","Mobile"],
# }
# key_list = []
# for key in contact_map:
#     if len(key) == 4:
#      key_list.append(key)                                      1st use
#      print(key_list)   
       
    


# key_trai = [key for key in contact_map if len(key) == 4]        '''2st use '''' same work
# print(key_trai)


                # ///////////////////////////////////

# Q.6: Create dictionary variable name world then inside it create countries dictionary, 
# Key will be the name country & country value will have another dictionary having capitalCity, currency and language to it. 
# by using any country key print all the value of Capital & Currency.


# world = {
#     "countries": {
#       "pakistan":{
#        "capital": "Islamabad",
#        "currency": "rupees",  
#        "language":  "Urdu"
#       },
     
#        "turkey":{
#         "capital":"Ankara",
#         "currency":"Turkish lira",
#         "language": "turkish"
#       },

#       "saudia_Arabia":{
#        "capital": "Riyadh",
#        "currency": "riyal", 
#        "language":  "Arbi" 
#       },

#        "uk":{
#        "capital": "London",
#        "currency": "pound", 
#        "language": "English"   
#       },

#       "usa":{
#        "capital": "Washington",
#        "currency": "dollar"    
#       },
#     }
# }
# print(world["countries"]["pakistan"])

# for country in world["countries"]:
#   capital =  world["countries"][country]["capital"] 
#   currency = world["countries"][country]["currency"] 
#   print(f"{country.title()}, Capital: {capital}, currency: {currency}")
#   print("-" * 30 )

        # ///////////////////////////////////



# Question 7 //
# Given a dictionary of expenses with days of the week as keys
# and corresponding values as amounts, check if "fri" exists in the dictionary. 
# If it exists, change its value to 5000.0. If it does not exist, 
# add "fri" to the dictionary with a value of 5000.0. 

# expenses = {
#     'sun': 3000.0,
#     'mon': 3000.0,
#     'tue': 3234.0
# }

# if 'fri' in expenses:
#     expenses['fri'] = 5000.0
#     print("'fri' already existed. Updated to 5000.0")
# else:
#     expenses['fri'] = 5000.0
#     print("'fri' added with value 5000.0")

# print(expenses)

         # ///////////////////////////////////

# Q.8: remove all false values from below list by using removeWhere 
# or retainWhere property.

# users_eligibility = [
#   {'name': 'yahya','eligibility': True},
#   # {'name': 'rais','eligibility': False},
#   {'name': 'yahya','eligibility': True},
#   # {'name': 'ahsan','eligibility': False},
#   # {'name': 'hasnain','eligibility': True},
# ]
# finallys = [key for key in users_eligibility if key['eligibility']]
# print(finallys)
# # filterd = []
# for user in users_eligibility:
#     if user ['eligibility']:
#      filterd.append(user)   

# print(f'{filterd} you are eligible')


       # ///////////////////////////////////

# Q.9 (Python):
# Given a list of integers, write a Python function that returns the maximum value
# from the list.

# num = [1,2,3,4,5,6,7,88]
# print(f"Greater Number :",max(num))

        
      # ///////////////////////////////////

# Q.10:
# Write a Python function that takes a list of strings
# and removes any duplicate elements, returning a new list without duplgit icates.
# The order of elements in the new list should be the same as in the original list.

# def remove_duplicates(input_list):
#     seen = set()  # To keep track of seen elements
#     result = []  # To store the result without duplicates
    
#     for item in input_list:
#         if item not in seen:
#             result.append(item)  # Add item to result if not seen before
#             seen.add(item)  # Mark item as seen
    
#     return result

# # Example usage:
# original_list = ["apple", "banana", "apple", "orange", "banana", "grape"]
# new_list = remove_duplicates(original_list)
# print(new_list)
# def greet(name):
#     print(f"Hello {name}!"

#         # /////////// 2nd option /////////

# fruits = [
#     "apple",
#     "apple",
#     "mango",
#     "orange",
#     "banana",
#     "banana"
# ]

# duplicate_elementsu = list(set(fruits))
# print(duplicate_elementsu)
# print(duplicate_elementsu)




# listiyo = [
#     'mango',
#     'apple',
#     'grapes'
#     'papaya',
#     'orange',
#     'mango'
# ]

# duplicateones = list(set(listiyo))
# print(duplicateones)


# listyo = ['hello',
#           'mango',
#           'grapes',
#           'grapes'
#          ]
# dupli = list(set(listyo))
# print(dupli)


fruites: list = ['apple','mango','grapes','papaya','banana']


  
# print(fruites[0])  
# print(fruites[-2])  
fruites.append('mango')
fruites.pop(1)
print(fruites)  
# print(fruites[0:3])  
  
fruto: list = ['apple','mango','pineApple','banana'] 
frutoer: list = ['apple','mango','pineApple','banana'] 
print(fruto.pop()) 
print(fruto.pop()) 

settiyo: set = ('hello world')
print(settiyo)
print(settiyo)










