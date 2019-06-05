#Remember to use sudo, otherwise the script cannot be ran via bash
#sudo pip3 install gspread
#sudo pip3 install --upgrade oauth2client
#sudo pip3 install PyOpenSSL

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
import socket
from subprocess import check_output

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('/home/pi/VRBike/rpiLogger-7f57ed4f3faf.json', scope)    # change this path to your own json credentials
gc = gspread.authorize(credentials)

####if you are creating a new spreadsheet using code####
# sh = gc.create("VRBike_Pi")
# sh.share('zbw18@uw.edu', perm_type='user', role='writer') # put the google account you want to share
# worksheet = sh.sheet1

####if using a pre-existing spreadsheet or creating a new one from the web interface####
worksheet = gc.open("VRBike_Pi").sheet1 #name of the spreadsheet

## Get IP  
IPAddr = PI_IP =  check_output(['hostname', '-I']).decode("utf-8") 

print("Start sending ...")
list_of_lists = worksheet.get_all_values()
line = len(list_of_lists)
worksheet.add_rows(line + 2)
worksheet.update_cell(line, 1, str(datetime.datetime.now()))
worksheet.update_cell(line, 2, str(IPAddr))
print("Finished")
