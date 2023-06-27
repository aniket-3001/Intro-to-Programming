import csv

with open("IP TUTS/TUT-8/Extra/data.csv") as input_file, open("IP TUTS/TUT-8/Extra/new_data.csv", 'w', newline='') as output_file:
    # Create a DictReader and DictWriter objects
    reader = csv.DictReader(input_file)
    writer = csv.DictWriter(
        output_file, fieldnames=reader.fieldnames + ['average'])

    # Write the header row to the output file
    writer.writeheader()

    # Loop through each row of the input file
    for row in reader:
        # Calculate the average marks for each student
        average_marks = sum([int(row['science']), int(row['maths']), int(
            row['sst']), int(row['english']), int(row['hindi'])]) / 5

        # Add the average_marks field to the row dictionary
        row['average'] = average_marks

        # Write the updated row to the output file
        writer.writerow(row)
