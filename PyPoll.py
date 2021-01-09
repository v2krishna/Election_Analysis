#Psuedo Code 
#Read the File
#total Votes
#List of Each Candidate
#Vote count for each candidate
#Percentage of Each Vote Count
#Winner of the election

import datetime as dt
import csv 
import os


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

    #for line in file_reader:
        #print()
    #print the file object
    
    print(election_data)


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

    # print(election_outputfile)
    election_outputfile.write(output_data)

