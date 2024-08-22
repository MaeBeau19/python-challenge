import os, csv
file_to_load = "./election_data.csv"

total_votes = 0
candidate_options = []
candidate_votes = {}

winning_candidate = ""
winning_count = 0

with open(file_to_load) as elec_file:
    reader = csv.reader(elec_file)

    header = next(reader)

    for row in reader:

        total_votes += 1
        candidate_name = row[2]

        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1





with open("elec_analysis.txt", "w")  as analysis:

    election_results = (
    f"Election Analysis\n"
    f"---------------------\n"
    f"Total Votes: {total_votes}\n"
    )
    print(election_results)
    analysis.write(election_results)

    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        votes_percentage = float(votes) / float(total_votes) *100

        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate

        voter_output = f"{candidate}: {votes_percentage:.2f}\n"
        print(voter_output)

    winning_candidate_summary = (
        f"-----------------\n"
        f"Winner: {winning_candidate}\n"
    )
    print(winning_candidate_summary)

    analysis.write(winning_candidate_summary)
            