# Election_Analysis

# Overview of the Election Audit

For this project, we were approached by oiur friend Tom, who is an employee at the Colorado Board of Elections. He asked for assistance in auditing a recent US Congressional Precinct election by conducting a vote count report to certify the election. THis process is usually domne in Excel, but they want to know if the procedures can be automated in Python. If it's successful, the code that Tom and I put tiogether could be used in the future for elections in other Congressional districts, in addition to Senatorial districts as well as local elections.

The dataset that we had access to included all votes cast in the election. There were three pieces of information for each volte:
- Ballot ID
- The county that the vote was cast in
- The candidate that the vote was cast for

# Election Audit Results

## County Level Results

- Voter Turnout for the Precinct

The total number of votes cast in the precinct for this election was 369,711.

- Voter Turnout by County

Since the borders of this Congressional district cover a wide area, there were votes from residents from three different counties. The number (and percentage) of ballots cast in each county was 306,055 in Denver (82.8%), 38,855 (10.5%) in Jefferson and 24,801 (6.7%) in Arapahoe. 

- County With the Largest Voter Turnout

The county with the highest number of votes was Denver, by a large margin. Almost 83% of all votes in this election were from this county.

## Candidate Results

- Candidate Performance

There were three candidates in this election. Diana DeGette received 272,892 votes, 73.8% of all votes cast. Charles Casper Stockham received 85,213 votes, 23.0% of the total. Raymon Anthony Doane received 11,606 votes, which was just 3.1% of all votes cast.

- Election Outcome

The winner of this US Congressional election was Diana DeGette, with 272,892 votes (73.8% of the total)

Election Audit Summary Table
![summary table](https://github.com/brianbutler08/Election_Analysis/blob/main/Election_Analysis/VS%20Code%20election%20output.png)

# Election Audit Summary

In addition to successfully auditing the Congressional election, Tom and I developed a piece of code that can be used fo future elections in the state (or elsewhere), no matter how large or small. As a best practice, we consciously did not hard code any specific numbers into our work. We could have easily used data specific to this election for some of the mathematical expressions, but chose to keep it flexible and allow the code to determine what the parameters were. A basic example of this is the establishment of a variable (total_votes) to count and hold the number of votes cast. We could have used the number 369,711 in our code when it was time to calculate percentages, but that would have complicated its use in other elections (with different vote totals). Similarly, we didn't include the actual names of the three candidates, but instead allowed the code to pull those from the dataset. These simple decisions allow the code to be applied to other elections with minimal, if any, adjustments.



Three distinct types - mail-in ballots, punch cards and Direct Recording Electronic
