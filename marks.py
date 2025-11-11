import sys
if len(sys.argv) == 6:

    script_name = sys.argv[0]
    marks1 = (sys.argv[1])
    marks2 = (sys.argv[2])
    marks3 = (sys.argv[3])
    marks4 = (sys.argv[4])
    marks5 = (sys.argv[5])

else:
    script_name = sys.argv[0]
    marks1 = 85
    marks2 = 90
    marks3 = 78
    marks4 = 92
    marks5 = 88
    print("Inputs not provided. Using default marks.")

total_marks = int(marks1) + int(marks2) + int(marks3) + int(marks4) + int(marks5)
average_marks = total_marks / 5

print("Script Name:", script_name)
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)

if average_marks >= 90:
    print("Grade: A")
elif average_marks >= 80:
    print("Grade: B")
elif average_marks >= 70:
    print("Grade: C")
elif average_marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")
