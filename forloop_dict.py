# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# for county in counties_dict:
#     print(county)


# for county in counties_dict.keys():
#     print(county)

# for k,v in counties_dict.items():
#     print(k, v)
    
# for county in counties_dict:
#     print(county, counties_dict[county])

# for county in counties_dict:
#     print(county, counties_dict.get(county))


# for county in counties_dict:
#     print(f"{county} has {counties_dict.get(county)} registered voters")


voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict['county'] , county_dict['registered_voters'])