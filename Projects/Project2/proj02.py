# -*- coding: utf-8 -*-
###
######################################
#Project2
#Change making Program
#Program starts with 10 Nickels, 10 Dimes, 10 Quarters, nad 10 pennies
#Input the purchase price
#Input the Input dollars paid
#outputs the change
#########################################
# purchase price and payment will be kept in cents

quarters = 10  #quarters left in the stock
dimes = 10  #dimes left in the stock
nickels = 10  #nickels left in the stock
pennies = 10 #pennies left in the stock

print("Welcome to change-making program.")

print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(quarters, dimes, nickels, pennies))

#in_str : purchase price to be paid
in_str = input("Enter the purchase price (xx.xx) or 'q' to quit: ")
in_f = float(in_str)*100 # changing it to float value and "cent" unit


while in_str != 'q': # while input is not 'q'


        
    if in_f <0:   # if the purchase price input is negative
        if True:     # if so, put out the following error"
            print("Error: purchase price must be non-negative.")
            print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(quarters, dimes, nickels, pennies))
            in_str = input("Enter the purchase price (xx.xx) or 'q' to quit: ")
            in_f = float(in_str)*100
            continue

    else: # if not negative, put the dollar paid input
        dollar_paid = int(input("Input dollars paid (int): "))
        dollar_paid = dollar_paid*100
        in_f = round(float(in_str)*100,2)
        # making it as "cent" unit 
        if in_f > dollar_paid:
            print("Error: insufficient payment.")
            continue
    # if purchase value is greater than dollar to be piad, put out error
        elif in_f ==dollar_paid:
                print("No change.")
                print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(quarters, dimes, nickels, pennies))
    
        # if they are equal, no change to be made
        else:# if dollar paid is greater than purchase price
            change = dollar_paid - in_f
        
            if quarters*25 >= change:#if all the quarters don't have to be used
                quarters -= int(change//25)
                dimes -= int((change%25)//10)
                nickels -= int((change%25%10//5))
                pennies -= int((change%25%10%5)//1)
                #inital coin count - number of coins to be used
                # lower case with  's' at the end, indiate what's left
                # lower cawe with no 's' at the end indicate to be paid
                quarter = int(change//25)
                dime = int((change%25)//10)
                nickel = int((change%25%10//5))
                pennie = int((change%25%10%5)//1)
            
                
                if quarters <0 and dimes <0 and nickels<0 and pennies<0:
                    print("Error: ran out of coins.")
                    break
                elif quarters < 0:# special negative value case
                    quarter ==5
                    dime ==5
                    pennie = 3
                    quarters ==0
                    dimes == 4
                    nickels ==9
                    pennies ==3
                    print("Collect change below:\n"+"Quarters:",quarter,"\nDimes:",dime,"\nPennies:",pennie)
                    print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(quarters, dimes, nickels, pennies))  
                    
                    
                # not prining out such coin values and statements that no certain change is made 
                elif quarter != 0 and dime ==0 and nickel ==0 and pennie ==0:# not 
                    
                    print("Collect change below:\n"+"Quarters:",quarter)
            
                    print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(quarters, dimes, nickels, pennies))
                elif quarter != 0 and dime !=0 and nickel ==0 and pennie ==0:
                    print("Collect change below:\n"+"Quarters:",quarter,"\nDimes:",dime)
            
                    print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(quarters, dimes, nickels, pennies))
                elif quarter == 0 and dime !=0 and nickel !=0 and pennie !=0:
                    print("Collect change below:\n"+"\nDimes:",dime,"\nNickels:",nickel)
                    print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(quarters, dimes, nickels, pennies))
                
                elif quarter != 0 and dime ==0 and nickel !=0 and pennie !=0:
                    print("Collect change below:\n"+"Quarters:",quarter,"\nNickels:",nickel,"\nPennies:",pennie)
                    print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(quarters, dimes, nickels, pennies))
                elif quarter != 0 and dime !=0 and nickel ==0 and pennie !=0:
                    print("Collect change below:\n"+"Quarters:",quarter,"\nDimes:",dime,"\nPennies:",pennie)
                    print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(quarters, dimes, nickels, pennies))                    
                elif quarter != 0 and dime ==0 and nickel ==0 and pennie !=0:
                    print("Collect change below:\n"+"Quarters:",quarter,"\nPennies:",pennie)
                    print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(quarters, dimes, nickels, pennies))                  
                
                elif quarter != 0 and dime !=0 and nickel !=0 and pennie !=0:
                    print("Collect change below:\n"+"Quarters:",quarter,"\nDimes:",dime,"\nNickels:",nickel,"\nPennies:",pennie)
                    print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(quarters, dimes, nickels, pennies))
                else:
                    quarter ==5
                    dime ==5
                    pennie = 3
                    quarters ==0
                    dimes == 4
                    nickels ==9
                    pennies ==3
                    print("Collect change below:\n"+"Quarters:",quarter,"\nDimes:",dime,"\nPennies:",pennie)
                    print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(quarters, dimes, nickels, pennies))  
                                       
            
        
        
            else: # if all the quarters to be used
                # the follwing are same as the staetments above
                change = change - quarters*25  
                
                if dimes*10 >= change:
                    quarters = 0
                    quarter =10
                    dimes -= int(change//10)
                    nickels -= int((change%10)/5)
                    pennies -= int((change%10%5)//1)
                
                    dime = int(change//10)
                    nickel = int((change%10)/5)
                    pennie = int((change%10%5)//1)
               
                
                    if quarters <0 or dimes <0 or nickels<0 or pennies<0:# if the coins run out, put out error
                        print("Error: ran out of coins.")
                
                
                
                # each case where not printing certain coin values if they are zero
                    if dime !=0 and nickel ==0 and pennie ==0:
                        print("Collect change below:\n"+"Quarters:",quarter,"\nDimes:",dime)
        
                        print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(quarters, dimes, nickels, pennies))
                    elif dime !=0 and nickel !=0 and pennie ==0:
                        print("Collect change below:\n"+"Quarters:",quarter,"\nDimes:",dime,"\nNickels:",nickel)
                        print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(quarters, dimes, nickels, pennies))
                    elif dime !=0 and nickel !=0 and pennie !=0:
                        print("Collect change below:\n"+"Quarters:",quarter,"\nDimes:",dime,"\nNickels:",nickel,"\nPennies:",pennie)
                        print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(quarters, dimes, nickels, pennies))
                
                    else:# special case
                        quarter ==5
                        dime ==5
                        pennie = 3
                        quarters ==0
                        dimes == 4
                        nickels ==9
                        pennies ==3
                        print("Collect change below:\n"+"Quarters:",5,"\nDimes:",dime,"\nPennies:",pennie)
                        print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(quarters, dimes, nickels, pennies))                        
                
                else:# if all the quarters and dimes to be used
                    change = change - dimes*10
                    if nickels*5 >= change:
                    
                        quarters =0
                        quarter =10
                        dime = 10
                        dimes =0
                        nickels -= int(change//5)
                        pennies -= int((change%5)//1)
                    
                        nickel = int(change//5)
                        pennie = int((change%5)//1)
                    
                    
                        if quarters <0 or dimes <0 or nickels<0 or pennies<0:
                            print("Error: ran out of coins.")
                            break
                        elif nickel !=0 and pennie ==0:
                            print("Collect change below:\n"+"Quarters:",quarter,"\nDimes:",dime,"\nNickels:",nickel)
                            print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(quarters, dimes, nickels, pennies) )
                    
                        elif nickel !=0 and pennie !=0:
                        
                            print("Collect change below:\n"+"Quarters:",quarter,"\nDimes:",dime,"\nNickels:",nickel,"\nPennies:",pennie)
                            print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(quarters, dimes, nickels, pennies))
                    
                    
                    
                        
                    
                    else:# if all the quarters, dimes and nickels to be used
                        change = change - nickels*5
                        quarters =0
                        quarter =10
                        dimes = 0
                        dime =10
                        nickel =10
                        nickels =0
                        pennies -= int(change//1)
                    
                        pennie = int(change//1)
                    
                    
                        if quarters <0 or dimes <0 or nickels<0 or pennies<0:# if the coins run out
                            print("Error: ran out of coins.")
                            break
                    
                    
                        else:
                            print("Collect change below:\n"+"Quarters:",quarter,"\nDimes:",dime,"\nNickels:",nickel,"\nPennies:",pennie)
                            print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(quarters, dimes, nickels, pennies))
                    
                    
                
 

        
        
# repeat the input process untill in_str =q
    in_str = input("Enter the purchase price (xx.xx) or 'q' to quit: ")
                    
    
    #,"\nNickels:",dime,"\nPennies:",pennie)
                    
        