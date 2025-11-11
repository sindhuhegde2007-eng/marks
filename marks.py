import sys
if len(sys.argv) != 6:
    print("Usage: python average_marks.py mark1 mark2 mark3 mark4 mark5")
    sys.exit(1)
marks = [int(sys.argv[i]) for i in range(1, 6)]
average = sum(marks) / 5
print("Marks entered:", marks)
print("Average marks:", average)
