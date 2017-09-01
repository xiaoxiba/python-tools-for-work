import os
            
if __name__ == '__main__':

    #print information for user reference
    print('=============usage notice==================================================')
    print('Compare two device connection of two design')
    print('command input as : design1 device1_1 device1_2 design2 device2_1 device2_2')
    print('===========================================================================')

    
    # get parameters
    ref_design, ref_dev1, ref_dev2, new_design, new_dev1, new_dev2 = input("Enter Parameters: ").split(' ')
    print('parameters:', ref_design, ref_dev1, ref_dev2, new_design, new_dev1, new_dev2)
    
    
    #open reference design .dat file
          
    
    #design_netlist.rpt contains info arrange by net name
    with open('.\\'+ ref_design + '\\packaged\\design_netlist.rpt','r') as ref_netlist:
        for each_line in ref_netlist:
            print(each_line) 
            #get ref_dev1 pin list

            for each_item in each_line.split(' '): #split each line to small items
                if each_item.find(ref_dev1):   #find the items contains ref_dev1 name
                    _, pin = each_item.split('.') #store pin number in pin
                    
                print(each_item, '\n')
 #               ref_dev1_pins
  #              each_line
            
                pass
            