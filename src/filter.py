import csv;

input = "HN_posts_year_to_Sep_26_2016.csv"
output = "filtered_hn.csv"

with open(input, mode='r', encoding='utf-8') as infile:
    # create csv_reader object
    csv_reader = csv.reader(infile)

    headers = next(csv_reader)

    filtered_rows = [headers]

    for row in csv_reader:
        if int(row[4]) > 1:
            filtered_rows.append(row)

with open(output, mode='w', newline='', encoding='utf-8') as outfile:
    csv_writer = csv.writer(outfile)

    csv_writer.writerows(filtered_rows)

print("Filtered data written to {output}")