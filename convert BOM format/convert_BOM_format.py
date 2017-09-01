
import os
import csv
import string



def convert_BOM_format(file_name):
    """ input file is .csv file with nvpn and mfgpn on each line
    """   
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        dict_location = {}
        # make {nvpn : location} dictionary from csv file
        for row in reader:       #check each row of csv file
            nvpn = row['NVPN']
            locations = row['LOCATION']
            
            location_split = locations.split(', ') #split each line to a python list for real nvpn line
            for location in location_split:
                dict_location[location] = nvpn  
    return dict_location

    
if __name__ == '__main__':

    #print information for user reference
    print('=============usage notice==================================================')
    print('The NVPN list is in nvpn.csv file, with "NVPN" colum for NVPN and "LOCATION" colum for component location')
    print('===========================================================================')


    #convert BOM to location based dictionary
    file_name = 'nvpn_location.csv'
    dict_location = convert_BOM_format(file_name)

    #record location based BOM into txt file
    with open('.\\converted_BOM.txt','w') as bom_file:
        for location in sorted(dict_location):
            bom_file.write(location + ',' + dict_location[location] + '\n')       
        print('converted BOM is recorded in .\\converted_BOM.txtt, please check')
    
          
    print('Done.')




