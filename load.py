# load information and initialize roster

# all input from CSV file

# key pair zalen
# vakken per key value met meerdere waardes.
# key value where key is studentnumber and value is rest

import csv
with open('input_files/studenten_roostering_1.csv', 'r') as csvfile:
    try:
        student = csv.reader(csvfile)
        break
    except LookupError:
        print ""
    except:
        print "Can not open the selected file"

    for row in student:
        # store info per row
