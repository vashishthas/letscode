#Basic school Administration tool
import csv
def write_into_csv(info_list):
    with open('stdinfo.csv','a',newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        if csv_file.tell()==0:
            writer.writerow(["Name","Age"])
        
        writer.writerow(info_list)

if __name__ == '__main__':  #main function
    condition=True
    stdnum=1
    while(condition):
        stdinfo=input("Enter student info for student #{} in the following manner Name Age: ".format(stdnum))
        #print(stdinfo)
    
        #split
        stdinfo_list=stdinfo.split(' ')
        #print("Split up info: " + str(stdinfo_list))
        
        print("\nThe Entered information is: -\nName: {}\nAge: {}".format(stdinfo_list[0],stdinfo_list[1]))
        
        choice= input("is the entered info correct? y/n: ")
        if(choice=='y'):
            write_into_csv(stdinfo_list)
            stdnum+=1
            check=input("Enter y/n for another student ")
            if(check=='y'):
                condition=True
            elif(check=='n'):
                condition=False
        elif(choice=='n'):
            print("Re-enter the values!")
            
