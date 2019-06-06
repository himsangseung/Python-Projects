# -*- coding: utf-8 -*-
"""
Project5
using GMO crops data from 2000-2016 to compute max, min, etc.
using dictionary to organize the data
inputs the file and ouputs orgnized data by state
"""

STATES = ['Alaska', 'Alabama', 'Arizona', 'Arkansas', 'California', 'Colorado\
          ', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho\
          ', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana\
          ', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', '\
          Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hamp\
          shire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'N\
          orth Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode \
          Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'U\
          tah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wiscon\
          sin', 'Wyoming']
# name of the states will be used for the testing

filename = input("Enter a file: ")
# asking for the input of the file name

def open_file(filename):
    '''
    this function opens the file whose name is inserted by the user. 
    try and except method to be used to reprompt for input if the input
    is something that outputs an error afterall
    it returns the datafile
    '''
    while True:
        try:# try opening the file with given input
            fp = open(filename)
            return fp
            break
        except:# if fails, ask again
            filename = input("Enter a file: ")

def display(dicts):
    '''
    this function takes the organized dictionary from readfile function
    and displays the output. set method was used to have orbitrary input.
    then orgnaized as a list to have sorted and iterate.    
    '''
    
    a= set()# empty set generated
    for items in dicts:# serach for the dictionary keys
        for items2 in dicts:# one more depth in to finding keys of it
            a.add(items2)# add on to the set
    a = list(sorted(a))        # make it as a sorted list
    
    for items in a:#  print orbitrary crops
        print()
    
    
        print("Crop: "+items)
        print("{:<20s}{:<8s}{:<6s}{:<8s}{:<6s}".format('State','Max Yr','Max',\
              'Min Yr','Min'))
        #prining the headline of the output
        
        for key,value in sorted(dicts[items].items()):
                print("{:<20s}{:<8d}{:<6d}{:<8d}{:<6d}".format(key,value\
                      ['max_year'],value['max_val'],value['min_year'],\
                      value['min_val']))  

        #separate the dicionary so that keys and items are to be printed
    
def read_file(fp):
    '''
    this function takes the data to read and returns a dictionary.
    empty dictionary is created and items are added on. 
    the data needed to be polished with strip, split method and isdigit(),etc
    '''
    dicts ={}# creating empty dicationary
    fp.readline()# skip the headline which is not to be used
    for lines in fp:# go with each line
        lines = lines.strip().split(',')# polishing data
        state = lines[0]
        crop = lines[1]
        variety = lines[3]
        year = int(lines[4])
        value = lines[6]
        if  not value.isdigit(): # if value is not digit, ignore this line
            continue
        if value.isdigit():# if the value is digit, use it make it a integer 
            value = int(value)
            
        if 'All GE varieties' in variety:# only using GE variety
            if 'U.S' in lines[0]:# polishing data, U.S row not to be used
                continue
            if 'Other States' in lines[0]: # other states row not to be used
                continue

            if 'Missouri' in state:#polishing data ignore '2/' 
                if '2/' in state:
                    state = state[:9]
                    lines[0] =state
                if '.' in state: # with in missouri ignore '.' in state
                    continue
                
            if crop not in dicts:# adding up the dictionary
                
                dicts[crop] ={}
            if state not in dicts[crop].keys():
                dicts[crop][state] = {"max_year":year, "max_val":value,\
                     "min_year":year,"min_val":value}
                # using a dicationary within dictionaries to organize the data
                # seting the default(first) value for varaible 'value'.
            if dicts[crop][state]["max_val"]< value:
                dicts[crop][state]["max_val"] = value
                dicts[crop][state]["max_year"] =year
                #compareing to get max value and year
                #if value less than last, update
            if dicts[crop][state]["min_val"] >value:
                dicts[crop][state]["min_val"] = value 
                dicts[crop][state]["min_year"] =year
                #compareing to get min value and year
                #if value bigger than last, update
            if dicts[crop][state]["max_val"] == value:
                if dicts[crop][state]["max_year"] > year:
                    dicts[crop][state]["max_year"] = year
            if dicts[crop][state]["min_val"] == value:
                if dicts[crop][state]["min_year"] > year:
                    dicts[crop][state]["min_year"] = year    
                # if the values are equal, use the lower number of year                            
    
    return dicts             #returns the organized dictionary

        
    fp.close()           



def main():
    '''
    main function which executes all the subfunctions including opening the
    file, reading the file and then finally displaying it
    '''
    fp = open_file(filename)    
    dicts = read_file(fp)
    display(dicts)

if __name__ =="__main__":
    main()