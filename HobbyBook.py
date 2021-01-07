print("Hello")

pets_dict = {
    "name":"rocky",
    "age" : "3",
    "hobbies": ['sleeping', 'jumping', 'outing'],
    "wakeup_during_wk": {"morning" : "5:00AM", "night": "11:00PM" }
}

print(f'Pet Name : {pets_dict["name"]}')
print(f'Number of Hobbies: {len(pets_dict["hobbies"])}')
print(f'Favorite Hobbies: {pets_dict["hobbies"][0]}')
print(f'Wake during Day: {pets_dict["wakeup_during_wk"]}')