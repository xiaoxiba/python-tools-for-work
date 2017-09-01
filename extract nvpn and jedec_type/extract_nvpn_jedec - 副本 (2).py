import os


def file2dict(file_name):
    """ input file is ptf file from P4
    """   
    

            
if __name__ == '__main__':

    #print information for user reference
    print('=============usage notice==================================================')
    print('Extract NVPN and JEDEC_TYPE of all ptf file')
    print('===========================================================================')

    
    # get parameters
    #ref_design, ref_dev1, ref_dev2, new_design, new_dev1, new_dev2 = input("Enter Parameters: ").split(' ')

    file_name = 'standard1.ptf'   
    nvpn_jedec_dict = {}
    
    with open('.\\ptf\\common\\'+ file_name,'r') as ptf_file:
        print('test1')
        
        find_part = False
        find_nvpn = False
        is_description_line = True
        
        for each_line in ptf_file:
            #print(each_line) 
            
            # replace '=' with space for easy process
            each_line = each_line.replace('=','')
            each_line = each_line.replace('  ',' ')
            
            each_line_split = each_line.split(' ') #split each line to a python list
            line_split_comma = each_line.split('\' \'') #split each line to a python list for real nvpn line
            
            if each_line.split(' ')[0] == 'PART':  #recored the start of finding nvpn, ignore begining for document
                find_part = True
                part = each_line_split[1]  #record what part
                print(each_line)
                continue
            if ('END_PART\n' in each_line_split):  # end of PART
                find_part = False
                print(each_line)
                continue                
       
            if (find_part is True) and ('NV_PN' in each_line_split):  #recored the start of finding nvpn, ignore begining for document
                
                find_nvpn = True
                is_description_line = False

                #for each_item in each_line_split:
                nvpn_index = each_line_split.index('NV_PN')
                jedec_index = each_line_split.index('JEDEC_TYPE')
                print(nvpn_index)
                print(each_line_split[nvpn_index])
                print(jedec_index)
                print(each_line_split[jedec_index])                
                continue
            
            if find_part and find_nvpn and not(is_description_line):
                #extract nvpn
                print(nvpn_index)
                nvpn = line_split_comma[nvpn_index]
                
                #extract JEDEC_TYPE
                jedec_type = line_split_comma[jedec_index]
                
                #record in dictionary
                nvpn_jedec_dict[nvpn] = jedec_type
                
                print(nvpn, jedec_type)
    
           

            