#Conditional Statments
"""
#if can be standalone
score = 100
if score >= 90:
    print("A")

#else can have no conditions, is optional but always need if statment   

score = 50
if score >= 90:
    print("A")
else:
    print("F")

#elif and nested if i have good enough understanding
score = 50
submitted_project = True
if score >= 90:
    if submitted_project:
        print("A+")
    else:
        print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

#using conditional operators
score = 60
submitted_project = False
if score >= 90 and submitted_project:
    print("A+")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60 or submitted_project:
    print("D")
else:
    print("F")

#mutliple if statments, they are independent
score = 100
submitted_project = False

if score >= 90:
    print("High Score")
else:
    print("Low Score")

if submitted_project:
    print("Project is submitted")
else:
    print("Project is not submitted")
"""
#Inline if & Match case










