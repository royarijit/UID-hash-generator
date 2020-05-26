import csv
import hashlib

f_name = input("Enter name of csv file")
e_name = input("Enter name of event (all lowercase)")
hash_dict = {}


def hash_trim(email, event_name):
    uid_str = email+event_name
    hash_str = hashlib.md5(uid_str.encode())
    hash_string = hash_str.hexdigest()
    trim_hash = hash_string[0:10]
    hash_dict[email] = trim_hash


with open(f_name) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    row_count = 0
    for row in csv_reader:
        if row_count == 0:
            row_count += 1
        else:
            hash_trim(row[1], e_name)

with open('quizmania_with_UID.csv', mode='w') as csv_file:
    field_names = ['email', 'hash']
    writer = csv.DictWriter(csv_file, fieldnames=field_names)

    writer.writeheader()
    for cont in hash_dict:
        writer.writerow({'email': cont, 'hash': hash_dict[cont]})
