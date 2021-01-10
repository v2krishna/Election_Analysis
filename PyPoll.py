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
county_names =[]
county_votes={}
largest_turnout_county = ""
largest_turnout =0
largest_turnout_percent=0


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
        total_votes += 1 #counting the votes 

        candidate_name = line[2] #candidate_name
        county_name  = line[1]  #county_name

        #add candidate name to the list candidate_options, also add to the candidate_votes dict add assing to value 0
        if candidate_name  not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name]=0 #getting the candidate votes
        
        #add the county name to the county_names list if not present, also add to the county_votes dictionary and assign to value 0
        if county_name not in county_names:
            county_names.append(county_name)
            county_votes[county_name]=0

        candidate_votes[candidate_name] +=1 #add the votes of the candidate
        county_votes[county_name] +=1 # increment the vote count of the county        
    print(candidate_options)
    print(candidate_votes)
    #print the file object
    # print(election_data)

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
    
    election_results =(
            f"\nElection Results\n"
            f"------------------------\n"
            f"Total Votes : {total_votes:,}\n"
            f"------------------------\n"
    )
    print(election_results)
    election_outputfile.write(election_results)

    for county_name in county_names:
        cnty_votes_count = county_votes[county_name]
        cnty_vote_percent =float(cnty_votes_count)/float(total_votes) * 100
        county_results = (f"{county_name}: {cnty_vote_percent:.1f}% ({cnty_votes_count:,})")
        print(county_results)
        election_outputfile.write(county_results)

        #determine which county has got more votes
        if (cnty_votes_count > largest_turnout) and (cnty_vote_percent > largest_turnout_percent):
            largest_turnout = cnty_votes_count
            largest_turnout_percent = cnty_vote_percent
            largest_turnout_county = county_name
    
    largest_turnout_county_summary = (
                                f"------------------------\n"
                                f"Largest County Turnout: {largest_turnout_county}\n"
                                f"------------------------"
                                )
    print(largest_turnout_county_summary)

    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percent = float(votes)/float(total_votes) * 100
        candidate_results =  (f"{candidate_name}: {vote_percent:.1f}% ({votes:,})\n")

        print(candidate_results) # print the candidate_results 
        election_outputfile.write(candidate_results) # writing to the text

        if (votes>winning_count) and (vote_percent > winning_percent):
            winning_count = votes
            winning_percent = vote_percent
            winning_candidate = candidate_name
    
    winning_candidate_summary = (
                                f"----------------------------------\n"
                                f"Winner: {winning_candidate}\n"
                                f"Winning Vote Count: {winning_count:,}\n"
                                f"Winning Percentage: {winning_percent:.1f}%\n"
                                f"-----------------------------------\n"

                                )
    print(winning_candidate_summary)
    election_outputfile.write(winning_candidate_summary)
    # print(election_outputfile)
    #election_outputfile.write(output_data)
