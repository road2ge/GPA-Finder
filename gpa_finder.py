from __future__ import print_function
# Let's define some grade things.
cp_gpa = []
h_gpa = []
ap_gpa = []
average = 61
for whattonamethis in range(0, 40):
    cp_gpa.append(whattonamethis * .125)
    h_gpa.append(whattonamethis * .125 + .5)
    ap_gpa.append(whattonamethis * .125 + 1)

number_of_classes = int(input('How many classes were you enrolled in this year? '))
cp_classes = int(input('And how many of those classes were weighted CP (standard)? '))
h_classes = int(input('And how many of those classes were weighted Honors? '))
print('So that means you were enrolled in', (number_of_classes - cp_classes) - h_classes, 'AP classes.')
print('I\'m going to have to ask you some questions now. Unfortunately, I would make this',
       'sound a little smarter, but Python\'s way of getting input from you from the console is a little annoying. Bear with me though.')

gpas = []
for cp_class_grade in range(0, cp_classes):
    num_grade = int(input('What was your grade for one of your CP classes? '))
    gpa = cp_gpa[num_grade - 61]
    gpas.append(gpa)

for h_class_grade in range(0, h_classes):
    num_grade = int(input('What was your grade for one of your Honors classes? '))
    gpa = h_gpa[num_grade - 61]
    gpas.append(gpa)

for ap_class_grade in range(0, (number_of_classes - cp_classes) - h_classes):
    num_grade = int(input('What was your grade for one of your AP classes? '))
    gpa = ap_gpa[num_grade - 61]
    gpas.append(gpa)

total_gpa = 0.0    
for gpa in range(0, len(gpas)):
    total_gpa += gpas[gpa]

avg_gpa = total_gpa / len(gpas)
print('You\'re total weighted South Carolina GPA is ', avg_gpa, '!', sep='')