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
#    Create a dictionary named contact_map with keys "name" and "phone", and store some appropriate values in it.
#    Then, use a list comprehension to find all keys in the dictionary that have a length of 4 characters.

# contact_map = {
#    "name" : ["Yahya","Rais","siflf","kjfljdfsjfl"],
#    "phone"  : ["Infinix","Mobile"],
# }
# key_list = []
# for key in contact_map:
#     if len(key) == 4:
#      key_list.append(key)                                         '''1st use ''''
#      print(key_list)   

# key_trai = [key for key in contact_map if len(key) == 5]      '''2st use '''' same work
# print(key_trai)




# Q.6: Create dictionary variable name world then inside it create countries dictionary, 
# Key will be the name country & country value will have another dictionary having capitalCity, currency and language to it. 
# by using any country key print all the value of Capital & Currency.


# world = {
#    "countries": {
#      "pakistan": {
#           "Capital": "Islamabad",
#           "Currency": "rupees",
#           },
#            "turkey":{
#             "Capital":"Ankara",
#              "Currency":"Turkish lira"
#           },
#            "UK":{
#             "Capital":"London",
#              "Currency":"pound"
#           },  
#     }
# }

# for country in world["countries"]:
#     capital = world["countries"][country]["Capital"] 
#     currency = world["countries"][country]["Currency"]
#     print(f"{country} capital: {capital} currency {currency}")
# print(world)


world = {
    "countries": {
      "pakistan":{
       "capital": "Islamabad",
       "currency": "rupees"    
      },
     
       "turkey":{
        "capital":"Ankara",
        "currency":"Turkish lira"
      },

      "saudia_Arabia":{
       "capital": "Riyadh",
       "currency": "riyal"    
      },

       "uk":{
       "capital": "London",
       "currency": "pound"    
      },

      "usa":{
       "capital": "Washington",
       "currency": "dollar"    
      },
    }
}

for country in world["countries"]:
  capital =  world["countries"][country]["capital"] 
  currency = world["countries"][country]["currency"] 
  print(f"{country}, Capital: {capital}, currency: {currency}")