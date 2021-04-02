import csv
course = "AIDI"
group = "b"
day = "v"
with open('data/timetable.csv', 'r') as file:
    reader = csv.DictReader(file)
    #get a list of univcd ersities in the desired location
    
    
    output = [row for row in reader if row['Course'] == "Artificial Intelligence" 
                                    and row['Subject'] == "Applied Machine Learning" 
                                  and row["Day"] == "Tuesday"]
    #print(output)
    for o in output:
        print(o['Time'])
    print(output[0]['Time'] + "\nRoom No.: " + output[0]['Room'])
