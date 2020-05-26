#Basic school Administration tool for entering name and marks of students and calulating its sum.
import csv
def write_into_csv(info_list):
    with open('stdinfo.csv','a',newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        if csv_file.tell()==0:
            writer.writerow(["Name","Marks1","Marks2","Marks3","Sum"])
        
        writer.writerow(info_list)

if __name__ == '__main__':  #main function
    condition=True
    stdnum=1
    while(condition):
        stdinfo=input("Enter student info for student #{} in the following manner, Name of the student and his marks in 3 subjects: ".format(stdnum))
        #print(stdinfo)
    
        #split
        stdinfo_list=stdinfo.split(' ')
        #print("Split up info: " + str(stdinfo_list))
        
        print("\nThe Entered information is: -\nName: {}\nMarks1: {}\nMarks2: {}\nMarks3: {}".format(stdinfo_list[0],stdinfo_list[1],stdinfo_list[2],stdinfo_list[3]))
        
        choice= input("is the entered info correct? y/n: ")
        if(choice=='y'):
            #write_into_csv(stdinfo_list)
            sum=int(stdinfo_list[1])+int(stdinfo_list[2])+int(stdinfo_list[3])
            stdinfo_list.append(sum)
            write_into_csv(stdinfo_list)
            stdnum+=1
            check=input("Enter y/n for another student ")
            if(check=='y'):
                condition=True
            elif(check=='n'):
                condition=False
        elif(choice=='n'):
            print("Re-enter the values!")
            
'''

Enter student info for student #1 in the following manner, Name of the student and his marks in 3 subjects: Vashishtha 97 98 100

The Entered information is: -
Name: Vashishtha
Marks1: 97
Marks2: 98
Marks3: 100
is the entered info correct? y/n: y
Enter y/n for another student y
Enter student info for student #2 in the following manner, Name of the student and his marks in 3 subjects: Shaurya 95 96 97

The Entered information is: -
Name: Shaurya
Marks1: 95
Marks2: 96
Marks3: 97
is the entered info correct? y/n: y
Enter y/n for another student y
Enter student info for student #3 in the following manner, Name of the student and his marks in 3 subjects: Ritika 96 97 98

The Entered information is: -
Name: Ritika
Marks1: 96
Marks2: 97
Marks3: 98
is the entered info correct? y/n: n
Re-enter the values!
Enter student info for student #3 in the following manner, Name of the student and his marks in 3 subjects: Ritika 95 97 98

The Entered information is: -
Name: Ritika
Marks1: 95
Marks2: 97
Marks3: 98
is the entered info correct? y/n: y
Enter y/n for another student n

OUTPUT:

Name,Marks1,Marks2,Marks3,Sum
Vashishtha,97,98,100,295
Shaurya,95,96,97,288
Ritika,95,97,98,290

 '''
