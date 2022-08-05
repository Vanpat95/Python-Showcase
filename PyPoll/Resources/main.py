import os
import csv


with open('election_data.csv', encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    votecount = 0
    charlesvote = 0
    dianavote = 0
    raymonvote = 0
    winnervote = ''

    for row in csvreader:
        votecount = votecount + 1
        if((row[2]) == 'Charles Casper Stockham'):
            charlesvote = charlesvote +1
        if((row[2]) == 'Diana DeGette'):
            dianavote = dianavote +1
        if((row[2]) == 'Raymon Anthony Doane'):
            raymonvote = raymonvote +1
    if (raymonvote > dianavote):
        winnervote = "Raymon Anthony Doane"
    elif (raymonvote > charlesvote):
        winnervote = "Raymon Anthony Doane"
    elif (dianavote > raymonvote):
        winnervote = "Diana DeGette"
    elif (dianavote > charlesvote):
        winnervote = "Diana DeGette"
    elif (charlesvote > raymonvote):
        winnervote = "Charles Casper Stockham"
    elif (charlesvote > dianavote):
        winnervote = "Charles Casper Stockham"








print(f'Election Results')
print(f'______________________________')    
print(f' ')    #for spacing
print(f'Total Votes: ', votecount)
print(f'______________________________')    
print(f' ')    #for spacing
print(f'Charles Casper Stockham: ', round((charlesvote/votecount)*100, 3), '$ (', charlesvote, ')')
print(f'Diana DeGette: ', round((dianavote/votecount)*100, 3), '$ (', dianavote, ')')
print(f'Raymon Anthony Doane: ', round((raymonvote/votecount)*100, 3), '$ (', raymonvote, ')')
print(f'______________________________')    
print(f'Winner:  ', winnervote)
print(f'______________________________')  