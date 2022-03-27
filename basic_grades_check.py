grades_list = []
grades_total= 0
z = "Your grades are"
for x in range(1,5+1):
    grades_input = float(input("Please give the grades:  "))
    grades_list.append(grades_input)

for i in range(0,len(grades_list)):
    grades_total = grades_total+grades_list[i]
grades_average = (grades_total/500)*100
print(grades_average)
if grades_average<=40:
    print("You are fail")
elif grades_average<=50:
    print(z,"'E'")
elif grades_average<=60:
    print(z,"'C'")
elif grades_average<=70:
    print(z,"'B-'")
elif grades_average<=75:
    print(z,"'B+'")
elif grades_average<=80:
    print(z,"'A'")
elif grades_average<=90 and grades_average<=100:
    print(z,"'A+'")
else:
    print("Try again")