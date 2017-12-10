from decision_tree import build_tree
from decision_tree import print_tree
from decision_tree import print_leaf
from decision_tree import classify
import csv

training_data = []

with open('data.csv', encoding="utf8") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        new_row = []
        for item in row[0].split(','):
            new_row.append(item)
        training_data.append(new_row)

my_tree = build_tree(training_data)

print_tree(my_tree)
print()

testing_data = [
    ['висока','низька','низька','середня ']
]

for row in testing_data:
    print ("Передбачено: %s" %
           (print_leaf(classify(row, my_tree))))
