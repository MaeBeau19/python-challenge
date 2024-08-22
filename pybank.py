import os, csv

total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999]
total_net = 0

file_to_laod = "./budget_data.csv"

with open(file_to_laod) as financial_data:
    reader = csv.reader(financial_data)

    header = next(reader)

    first_row = next(reader)

    total_months += 1

    total_net += int(first_row[1])
    prev_net = int(first_row[1])


    for row in reader:

        total_months += 1
        total_net += int(row[1])

        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]
        month_of_change += [row[0]]

        if net_change > greatest_increase[1]:
            greatest_increase[1] = net_change
            greatest_increase[0] = row[0]

        if net_change < greatest_decrease[1]:
            greatest_decrease[1] = net_change
            greatest_decrease[0] = row[0]

net_monthly_avg = sum(net_change_list) / len(net_change_list)

output = (
    f"Financiall Data Analysis\n"
    f"-----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: {total_net}\n"
    f"Average income: {net_monthly_avg:.3f}\n"
    f"Greatest Incerase, month :{greatest_increase[0]}, value: {greatest_increase[1]:.3f} $\n"
    f"Greatest Decerase, month :{greatest_decrease[0]}, value: {greatest_decrease[1]:.3f} $\n"
)

print(output)

with open("analysis.txt", "w") as txt_file:
    txt_file.write(output)