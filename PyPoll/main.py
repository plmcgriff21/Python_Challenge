#import operating system path
import os 
#import csv interpreter
import csv
#create the file path
csvpath=os.path.join("PyPoll","Resources","election_data.csv")
#-------------------------------------------------------------
#Creating variables external to the loop
votecount=0
votecounter=[]
candidates=[]
khanvotes=0
correyvotes=0
livotes=0
otooleyvotes=0
# open the path with the reader
with open (csvpath) as csvreader:
#-------------------------------------------------------------
#Use the csv reader to translate the file for human viewers
    csvreader = csv.reader(csvreader,delimiter=',')
# identify the hearder row
    csv_header=next(csvreader)
    #print(csv_header)
#-------------------------------------------------------------
      
#Calculate the total number of votes
    for rows in csvreader:
        votecount=votecount+1
        votecounter.append(votecount)
        totalvotes=len(votecounter)
        allcandidates=(rows[2])
#Create a list of candidates
        candidates.append(allcandidates)
#Calculate number of Khan Votes
        if rows[2]=='Khan':
          khanvotes=khanvotes+1
#Caluclate number of votes for Correy
        if rows[2]=='Correy':
          correyvotes=correyvotes+1
#Calculate number of votes for Li
        if rows[2]=='Li':
          livotes=livotes+1
#Calculate number of votes for O'Tooley
        if rows[2]=="O'Tooley":
          otooleyvotes=otooleyvotes+1
        if khanvotes > correyvotes and livotes and otooleyvotes:
          winner="Khan"
          if correyvotes > khanvotes and livotes and otooleyvotes:
            winner="Correy"
            if livotes> khanvotes and livotes and correyvotes and otooleyvotes:
              winner="Li"
              if otooleyvotes>khanvotes and livotes and correyvotes and livotes:
                winner="O'Tooley"
              
with open("electionoutput.txt","a") as f:            
  print("-------Election Results-------------------",file=f)
  print(f'"Total Number of Votes Cast:"{totalvotes}',file=f)
  print(f'"List of Candidates:"{set(candidates)}',file=f)
  print(f'"Total Number of Khan votes:{khanvotes} Percent of Votes:{round(khanvotes/votecount*100.00,3)}%',file=f)
  print(f'"Total Number of Correy votes:{correyvotes} Percent of Votes:{round(correyvotes/votecount*100,3)}%',file=f)
  print(f'"Total Number of Li votes:{livotes} Percent of Votes:{round(livotes/votecount*100,3)}%',file=f)
  print("Total Number of O'Tooley votes:"f'{otooleyvotes} Percent of Votes:{round(otooleyvotes/votecount*100,3)}%',file=f)
  print(f'"Winner:"{winner}',file=f)
  print("----------------------------------------------------------------------------------------",file=f)



## PyPoll
#In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.
#You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). 
# The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. 
# Your task is to create a Python script that analyzes the votes and calculates each of the following:

#The total number of votes cast

#A complete list of candidates who received votes

#The percentage of votes each candidate won

#The total number of votes each candidate won

#The winner of the election based on popular vote.

#As an example, your analysis should look similar to the one below:

#Election Results
#-------------------------
#Total Votes: 3521001
#-------------------------
 #Khan: 63.000% (2218231)
 #Correy: 20.000% (704200)
  #Li: 14.000% (492940)
  #O'Tooley: 3.000% (105630)
#-------------------------
  #Winner: Khan
#-------------------------
 
#In addition, your final script should both print the analysis to the terminal and export a 
# text file with the results.