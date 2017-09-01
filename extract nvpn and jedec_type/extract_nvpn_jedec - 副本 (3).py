import os


def file2dict(file_name):
    """ input file is ptf file from P4
        output dictionary with {nvpn, jedec_type}
    """   
    nvpn_jedec_dict = {}
    
    with open(file_name,'r', encoding='gbk') as ptf_file:        
        find_part = False
        find_nvpn = False
        is_description_line = True
        
        for each_line in ptf_file:
            #print(each_line) 
            
            # replace '=' with space for easy process
            each_line = each_line.replace('=','')
            each_line = each_line.replace('  ',' ')
            
            line_split_space = each_line.split(' ') #split each line to a python list
            line_split_comma = each_line.split('\' \'') #split each line to a python list for real nvpn line
            
            if each_line.split(' ')[0] == 'PART':  #recored the start of finding nvpn, ignore begining for document
                find_part = True
                part = line_split_space[1]  #record what part
                continue
            if ('END_PART\n' in line_split_space):  # end of PART
                find_part = False
                continue                
       
            if (find_part is True) and ('NV_PN' in line_split_space):  #recored the start of finding nvpn, ignore begining for document
                
                find_nvpn = True
                is_description_line = False

                #for each_item in line_split_space:
                nvpn_index = line_split_space.index('NV_PN')
                jedec_index = line_split_space.index('JEDEC_TYPE')              
                continue
            
            if find_part and find_nvpn and not(is_description_line):
                #extract nvpn
                nvpn = line_split_comma[nvpn_index]
                
                #extract JEDEC_TYPE
                jedec_type = line_split_comma[jedec_index]
                
                #record in dictionary
                nvpn_jedec_dict[nvpn] = jedec_type
    return nvpn_jedec_dict

            
if __name__ == '__main__':

    #print information for user reference
    print('=============usage notice==================================================')
    print('Extract NVPN and JEDEC_TYPE of all ptf file')
    print('===========================================================================')

    
    # get parameters
    #ref_design, ref_dev1, ref_dev2, new_design, new_dev1, new_dev2 = input("Enter Parameters: ").split(' ')

    file_name = '.\\ptf\\common\\standard.ptf'
    #file_name = '.\\ptf\\common\\norm.ptf'

    nvpn_jedec_dict = file2dict(file_name)
    
    for nvpn, jedec_type in nvpn_jedec_dict.items():
        print (nvpn, jedec_type)
    

            