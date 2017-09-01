import os
import string

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

    #file_name = '.\\ptf\\common\\standard.ptf'
    #file_name = '.\\ptf\\common\\norm.ptf'
    nvpn_jedec_dict = {}
    
    
    #explore all ptf files
    base_path = '.\\ptf'
    list_dir = os.listdir(base_path)
    print(list_dir)  
    for directory in list_dir:
        file_names = os.listdir(os.path.join(base_path, directory))
        for file_name in file_names:
            print(file_name)
        
            path = os.path.join(base_path, directory, file_name)
            nvpn_jedec_dict_temp = file2dict(path)
            nvpn_jedec_dict = dict(nvpn_jedec_dict, **nvpn_jedec_dict_temp)  #join the dict
    
    #record dictionary into file
    with open('nvpn_jedec.txt','w') as result_file:
        for nvpn, jedec_type in nvpn_jedec_dict.items():      
            result_file.write(nvpn + ',' + jedec_type + '\n')       
        print('NVPN and JEDEC_TYPE is recorded in nvpn_jedec.txt, please check')
    


            