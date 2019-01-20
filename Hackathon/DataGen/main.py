import random


file = open("marklist.csv", 'w')
file2 = open("hourspent.csv", 'w')
physics = ["vectors", "newtons laws of motion", "kinemetics"]
chemistry = ["basic concepts of chem", "redox reactions", "gaseous theory"]
maths = ["trignometry", "logrithms", "integral calculus"]
sub_list = [physics, chemistry, maths]
counter = 1

file.write("Hash" + ',' "Total Marks" + ',' + "Physics" + ',' + physics[0] + ',' + physics[1] + ',' + physics[
    2] + ',' + "Chemistry" + ',' + chemistry[0] + ',' + chemistry[1] + ',' + chemistry[2] + ',' + "Maths" + ',' + maths[
               0] + ',' + maths[1] + ',' + maths[2] + '\n')
file2.write("Hash" + ',' + physics[0] + ',' + physics[1] + ',' + physics[
    2] + ",Tot Physics"  + ',' + chemistry[0] + ',' + chemistry[1] + ',' + chemistry[2] + ",Tot Chemistry"  + ',' + maths[
               0] + ',' + maths[1] + ',' + maths[2] + ",Tot Maths" + '\n')


while(counter <= 50):

    name = ""
    student_name = ""
    topic_name = ""
    for i in range(random.randint(0, 20)):
        student_name += chr(random.randint(65,90))
    for i in range(random.randint(0, 20)):
        topic_name += chr(random.randint(65,90))
    m = random.randint(0,2)
    n = random.randint(0,2)

    if m == 0:
        subject = "Physics"
    elif m == 1:
        subject = "Chemistry"
    else:
        subject = "Maths"
    print(sub_list[m][n])


    if random.randint(0, 1) == 1:
        pomodoro = '1'
    else:
        pomodoro = '0'

    chem = {}
    sum=0
    for i in chemistry:
        chem[i] = random.randint(-10, 40)
        sum += chem[i]
    chemmark = sum

    sum = 0
    math={}
    for i in maths:
        math[i] = random.randint(-10, 40)
        sum += math[i]
    mathmark = sum

    phy={}
    sum = 0
    for i in physics:
        phy[i] = random.randint(-10, 40)
        sum += phy[i]
    phymark = sum

    num = mathmark + phymark + chemmark
    print(mathmark , phymark , chemmark)
    file.write('# ' + ',' + str(num) + ',')
    file2.write('# ' +  ',')


    file.write(str(phymark) + ',')
    sum = 0
    for i in phy.values():
        file.write(str(i) + ',')
        file.write(str(i) + ',')
        num = random.randint(0, 5)
        file2.write(str(num) + ',')
        sum += num
    file2.write(str(sum) + ',')

    sum = 0
    file.write(str(chemmark) + ',')
    for i in chem.values():
        file.write(str(i) + ',')
        file.write(str(i) + ',')
        num = random.randint(0, 5)
        file2.write(str(num) + ',')
        sum += num
    file2.write(str(sum) + ',')

    sum = 0
    file.write(str(mathmark) + ',')
    for i in math.values():
        file.write(str(i) + ',')
        file.write(str(i) + ',')
        num = random.randint(0, 5)
        file2.write(str(num) + ',')
        sum += num
    file2.write(str(sum) + '\n')
    file.write('\n')



    counter += 1

file.close()
