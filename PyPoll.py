#Dependencies modules
import datetime as dt
import csv 
import os


#Initalizes the  variables
total_votes= 0
candidate_options=[]
candidate_votes={}
winning_candidate =""
winning_count =0
winning_percent = 0

print(f"The time right now is {dt.datetime.now()}")
# print(dir(csv))
# print(dir(os))

# file_variable  = open("Resources/election_results.csv", "r")
# print(file_variable)

# 1 Direct file path
#file_to_load = 'Resources/election_results.csv'
# election_data = open(file_to_load, "r")
# election_data.close()

#2 indirect file path using the os.path.join()
file_to_load = os.path.join("Resources","election_results.csv")

#Open  the election results and read the file


with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)

    for line in file_reader:
        #counting the votes 
        total_votes += 1


        #candidate_name
        candidate_name = line[2]

        #add candidate name to the list candidate_options
        if candidate_name  not in candidate_options:
            candidate_options.append(candidate_name)
            #getting the candidate votes
            candidate_votes[candidate_name]=0

        #add the votes of the candidate
        candidate_votes[candidate_name] +=1

        
        #print(total_votes) 
    print(candidate_options)
    print(candidate_votes)
    #print the file object
    # print(election_data)

for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]

    #percent of votes
    vote_percent = float(votes)/float(total_votes) * 100

    #print each candidate
    print(f"{candidate_name}: received {vote_percent:.1f}% for the votes")

    if (votes>winning_count) and (vote_percent > winning_percent):
        winning_count = votes
        winning_percent = vote_percent
        winning_candidate = candidate_name

print(f"{winning_candidate} has received {winning_count} with {winning_percent:.1f}")
#load the output data to  file 
file_to_save = os.path.join("analysis","election_analysis.txt")

#open the file to save 
with open(file_to_save, "w") as election_outputfile:
    
    # election_outputfile.write("Arapahoe, ")
    # election_outputfile.write("Denver, ")
    # election_outputfile.write("Jefferson, ")
    #election_outputfile.write("Arapahoe\nDenver\nJefferson")
    output_data = (f"\nArapahoe\n"
                   f"Denver\n"
                   f"Jefferson\n"
                  )
    winning_candidate_summary = (
        f"====================================\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percent:.1f}%\n"
        f"====================================\n"

                                )
    election_outputfile.write(winning_candidate_summary)
    # print(election_outputfile)
    #election_outputfile.write(output_data)


