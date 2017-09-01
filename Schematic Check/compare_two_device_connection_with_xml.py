import os
import xml.etree.ElementTree as ET 

def xml2dict(file_name,device_name):

  # return dictionary with {pin_name, net_name} list of device_name of file_name (xml file)
    with open('.\\' + file_name +'.xml','r') as file_xml:   
        tree = ET.parse(file_xml)
        root = tree.getroot()
        tag = root.tag  
        
        dict_pin_net = {}   #dictionary stor 
        
        nets = root.findall('net')
        for net in nets:
            net_id = net.find('id')
            net_name = net_id.text
            #print(net_name) 
            
            pins = net.findall('pin')
            for pin in pins:
                pin_id = pin.find('id')
                device_pin_name = pin_id.text
        
                #Get reference design devic info     
                if (device_name + '.') in device_pin_name:  #judge device name is matched
                    print(device_pin_name)
                    _, pin_name = device_pin_name.split('.')
                    print(pin_name)
                    dict_pin_net[pin_name] = net_name   #store {pin_name, net_name} in dictionary
    
    return dict_pin_net      


if __name__ == '__main__':

    #print information for user reference
    print('=============usage notice==================================================')
    print('Compare two device connection of two design')
    print('command input as : design1 device1_1 device1_2 design2 device2_1 device2_2')
    print('===========================================================================')

    
    # get parameters
    #ref_design, ref_dev1, ref_dev2, new_design, new_dev1, new_dev2 = input("Enter Parameters: ").split(' ')
    #print('parameters:', ref_design, ref_dev1, ref_dev2, new_design, new_dev1, new_dev2)
    ref_design, ref_dev1, ref_dev2, new_design, new_dev1, new_dev2 = 'P3489','U28','R215','P3310','R1','R2'
       
       
#Get reference desing info 
 
    
    dict_ref_dev1 = {}   #dictionary stor reference design device 1 {pin_name, net_name}
    dict_ref_dev2 = {}   #dictionary stor reference design device 2 {pin_name, net_name}

    dict_ref_dev1 = xml2dict(ref_design, ref_dev1)
    dict_ref_dev2 = xml2dict(ref_design, ref_dev2)
                
    for pin_name in sorted(dict_ref_dev1):
        print(pin_name, dict_ref_dev1[pin_name])
    for pin_name in sorted(dict_ref_dev2):
        print(pin_name, dict_ref_dev2[pin_name])


 
            