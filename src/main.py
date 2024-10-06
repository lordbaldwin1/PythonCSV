import pandas as pd;
import csv;
import datetime as dt;

input_file = "filtered_hn.csv"
# reading in csv with pandas
posts = pd.read_csv(input_file) # usecols=['id', 'num_points', 'num_comments'] parameter to drop other columns

# print(posts.head())

# reading in csv with built-in csv module
#Opens csv
with open(input_file, mode = 'r', encoding='utf-8') as file:
    # creates csv reader object
    posts_2 = csv.reader(file)

    # reads headers into a variable, after calling next it moves to the second row
    headers = next(posts_2)

    # converts csv after headers into a list of lists
    data = list(posts_2)

    # reads first 5 rows with splicing
    # for row in data[:5]:
        # print(row)
    
# print("Headers: \n", headers)

ask_posts = []
show_posts = []
other_posts = []

for row in data:
    title = row[1].lower()

    if title.startswith('ask hn'):
        ask_posts.append(row)
    elif title.startswith('show hn'):
        show_posts.append(row)
    else:
        other_posts.append(row)

print(len(ask_posts))
print(len(show_posts))
print(len(other_posts))

total_ask_comments = 0
total_show_comments = 0
total_other_comments = 0

for row in ask_posts:
    try:
        value = int(row[4])
        total_ask_comments += value
    except ValueError:
        print(f"Non-numeric value in row: {row}")

for row in show_posts:
    try:
        show_value = int(row[4])
        total_show_comments += show_value
    except ValueError:
        print(f"Non-numeric value in row: {row}")

for row in other_posts:
    try:
        other_value = int(row[4])
        total_other_comments += other_value
    except ValueError:
        print(f"Non-numeric value in row: {row}")

avg_ask_comments = total_ask_comments/len(ask_posts)
avg_show_comments = total_show_comments/len(show_posts)
avg_other_comments = total_other_comments/len(other_posts)

print("Average number of comments per ask post: ", avg_ask_comments)
print("Average number of comments per show post: ", avg_show_comments)
print("Average number of comments per other posts: ", avg_other_comments)

result_list = []

for row in ask_posts:
    new_row = [row[6], int(row[4])]

    result_list.append(new_row)

counts_by_hour = {}
comments_by_hour = {}








    
