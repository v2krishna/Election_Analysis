# my_votes =int(input("How many votes did you get in the election: "))
# total_votes = int(input("What is the total votes in the election: "))
# percentage_votes =(my_votes/total_votes)*100
# print(f"I received {percentage_votes} % of the total votes")

# candidate_votes = int(input("How many votes did the candidate get in the elections ?"))
# total_votes =int(input("What is the total number of votes in the election ?"))
candidate_votes = 33
total_votes = 75
percent_votes = (candidate_votes/total_votes)*100
message_to_candidate = (
                        f"you received {candidate_votes} number of votes. \n"
                        f"The total number of votes in the election was {total_votes}. \n"
                        f"You received {percent_votes:.2f} % of the total votes ")
print(message_to_candidate)