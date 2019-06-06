########################################################################
#Computer Project 6
#
#Using GDP.txt
#Finding the minimum and maximum GDP change for the years 1969 through 2015
#stateing the corresponding GDP values in trillions
#######################################################################
def open_file(): # insert file name until it is correct: GDP.txt
    filename = input('Enter a file name: ')
    Done = False
    while not Done:
        try:
            fileopen = open(filename,'r')
            Done = True
            return fileopen
        except FileNotFoundError:
            print("Error. Please try again")
            filename = input('Enter a file name: ')


def find_min_percent(line):
#Find the min percent change in the line; return the value and the index.
    min_val = float(100000)

    for j in range(0,564,12):
        if (float(str(line[76+j:+ 83+j]))) <min_val:
           min_val = (float(str(line[76+j:+ 83+j])))
           index_min= int((line.find(str(min_val))))-3
      
    return min_val,index_min
    '''
    min_val : minimum GDP value
    index_min : index that indicates where minimum GDP value is 
    '''
    

def find_max_percent(line):
#Find the max percent change in the line; return the value and the index.
    max_val = float(-500)# setting -500 values and keep comparing bigger values 
    for j in range(0,564,12): #12 characters spacing
        if (float(str(line[76+j:+ 83+j]))) >max_val:#charcter slicing
            max_val =  (float(str(line[76+j:+ 83+j])))
            index_max= int(line.find(str(max_val)))-4
       
    return max_val,index_max  
    '''
    max_val : maximum GDP value
    index_max : index that indicates where maximum GDP value is 
    '''
def find_gdp(line,index):#finding gdp values with corresponding index
    gdp =(line[index:index+8])
    gdp = float(gdp) # converting string to float value to compare
    return gdp
    '''
    gdp : corresponding GDP value according to index 
    '''    
    

#Use the index fo find the gdp value in the line; return the value

  
def find_year(line,index_min,index_max):# finding coresponding year with index
    min_year =(line[index_min:index_min+7])
    max_year = (line[index_max:index_max+7])
    return min_year,max_year
    '''
    min_year : year that minimum GDP change value indicates
    max_year : year that maximum GDP change value indicates
    '''
def display(min_val, min_year, min_val_gdp, max_val, max_year, max_val_gdp):
#Display values; convert billions to trillions first.  
    min_val_gdp = float(min_val_gdp)/1000
    max_val_gdp = float(max_val_gdp)/1000
#format of the output
    print("Gross Domestic Product")

    print("{:<10s}{:>8s}{:>6s}{:>18s}".format("min/max","change", "year", \
          "GDP (trillions)"))

    print("{:<10s}{:>8.1f}{:>6d}{:>18.2f}".format("min",min_val,int(min_year),\
          min_val_gdp))

    print("{:<10s}{:>8.1f}{:>6d}{:>18.2f}".format("max",(max_val),\
          int(max_year),max_val_gdp))

    '''
    min_val_ gdp : Maximum GDP value computed out from find_gdp
    max_val_ gdp : Maximum GDP value computed out from find_gdp
    '''   

def main():                    

#main run function, which includes all the subfunctiions will be used
    
    fileopen = open_file() # openning the file and store it as fileopen
    count = 0

    for line in fileopen:
        count  +=1 # counting the line number
        if count ==9: # when line9 execute the following:
            min_val,index_min = find_min_percent(line)
            #function for min change in gdp
            max_val,index_max = find_max_percent(line)
            #function for max change in gdp

            continue
        if count ==43: #line 43 indicates 'year'
            min_year,max_year = find_year(line,index_min,index_max)
            #find a year with coresponding max and min index values
            continue
    
        if count ==44:# line 44 indicates gdp values

            min_val_gdp= find_gdp(line,index_min)
            max_val_gdp = find_gdp(line,index_max)
       
    
    display(min_val, min_year, min_val_gdp, max_val, max_year, max_val_gdp)
    # display function to show output
if __name__ == "__main__":
    main()
