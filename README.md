# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given the following tasks to audit the election of recent local congressional Election.

1. Calculate the total number of votes cast.
1. List of candidates who received votes
1. Calculate the total number of votes each candidate received.
1. Calculate the percent of votes each candidate won.
1. Determine the winner of the election based on popular vote
1. Write the Election Results to a output file

### Resources
- Data Source: election_result.csv
- Tools: Python 3.7.8 , Visual Studio Code 1.52.1

## Election-Audit Results
Analysis of the recent election conducted in Colorado:
- There were 369,711 votes casted in the election.
- <b> List of candidates who received votes were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
    
#### County Election Summary
- List of counties are votes cast
  - Jefferson
  - Denver
  - Arapahoe
 
 - County Results , calculating the votes casted for all the candidates.
    - Arapahoe received 6.% vote with 38,855 number of vote
    - Denver received 82.8% vote with 306,055 number of votes
    - Jefferson received 6.7% vote with 24,801 number of votes
    
 - Based on the above results, the largest turnout county is : Denver
    
#### Candidate Results are:
   - Charles Casper Stockham received <b>10.5%</b> of the vote with <b>38,855</b> number of votes
   - Diana DeGette recieved 73.8% of the vote with 272,892 number of votes 
   - Raymon Anthony Doane received 3.1% of the vote with 11,606 number of votes
   
- The winner of the election was:
    - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes 
  
- Formatted Terminal Election Results Output <br/>
![colorado_election_results](/Resources/election_results_terminal.png) <br/>
- Text output of Election Results <br/>
![colorado_election_results_to_textfile](/Resources/election_results_textoutput.png) <br/>

## Election-Audit Summary
If The existing python script can be modified with following changes:

    - Allow the election auditor to enter the state
    - Folderpath where each state election results data are stored
    - Output file name, dynamically appends the state name at the end will allow store the election results for all states.
    
By doing these couple of changes, the python script can be used to get the election results of any state with just entering these two arguments. 
With some more modifications, we can make to have only one output file with all the election results appended to the same file as we run for multiple states.






    
    
