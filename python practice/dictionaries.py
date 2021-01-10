print("Hello World")


voting_data = []
voting_data.append({'county':'Arapahoe', 'registered_voters':422829})
voting_data.append({'county':'Denver', 'registered_voters':463353})
voting_data.append({'county':'Jefferson', 'registered_voters':432438})


no_of_counties = len(voting_data)
print(voting_data)


print(f"Number of Counties: {no_of_counties}")
for items in voting_data:
    print( items['county'], items['registered_voters'])


voting_data.append({'county':'El Paso', 'registered_voters':'461149'})
print(voting_data)                   
voting_data.remove({'county':'Arapahoe', 'registered_voters':422829})
print(voting_data)   
voting_data.remove({'county':'Denver', 'registered_voters':463353})
print(voting_data)   
voting_data.insert(3,{'county':'Denver', 'registered_voters':463353})


voting_data.insert(2,{'county':'Jefferson', 'registered_voters':432438})
print(voting_data)
voting_data.remove({'county':'Jefferson', 'registered_voters':432438})


voting_data.append({'county':'Arapahoe', 'registered_voters':422829})
print(voting_data)

