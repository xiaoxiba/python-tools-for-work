import os
            
if __name__ == '__main__':

    #print information for user reference
    print('=============usage notice==================================================')
    print('Compare two device connection of two design')
    print('command input as : design1 device1_1 device1_2 design2 device2_1 device2_2')
    print('===========================================================================')

    
    # get parameters
    #ref_design, ref_dev1, ref_dev2, new_design, new_dev1, new_dev2 = input("Enter Parameters: ").split(' ')

    file_name = 'standard1.ptf'   

    with open('.\\ptf\\common\\'+ file_name,'r') as ptf_file:
        print('test1')
        for each_line in ptf_file:
            #print(each_line) 

            i = 0
            each_line_split = each_line.split(' ') #split each line to small items
            for each_item in each_line_split:
                #if each_item.find('PART'):   # find PART defination start
                #    start_part = TRUE;
                #    continue;
                
                if 'NV_PN' in each_item:   # find NVPN defination location
                    #index = each_line_split.find('NV_PN')
                    print(i)
                    print(each_line_split[i])
                    break
                i = i + 1
            for 
            
               # if each_item.find('NV_PN'):   #find the items contains NV_PN
                    #_, pin = each_item.split('.') #store pin number in pin
                    
              #      print(each_item, '\n')
            
                pass
            