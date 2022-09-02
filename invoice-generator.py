#!/usr/bin/python3
# Python v3.8.10
# pip install openpyxl xlsxwriter
import openpyxl
from datetime import date  
import json


# Read sellers file
sellerfile = open('seller.json',)
sellerdata = json.load(sellerfile)
sellerfile.close()

# Read clients file
clientsfile = open('clients.json',)
clientdata = json.load(clientsfile)
clientsfile.close()

# Generate data strings
getDate = date.today() 
datetoday = str(getDate.month)+ "/" + str(getDate.day) + "/" + str(getDate.year)   
datetodayout = str(getDate.month)+ "-" + str(getDate.day) + "-" + str(getDate.year)   

# Read Excel (or any xls)
xfile = openpyxl.load_workbook("template.xlsx")
sheet = xfile["Invoice"]

#---------------------------
# Populate data :D 
#---------------------------

# Fix rows
sheet['A2'] = 'SELLER'
sheet['B2'] = 'BUYER'
sheet['D2'] = 'INVOICE'
sheet['D3'] = 'No.'
sheet['D4'] = 'Issue Date:'
sheet['D5'] = 'Due Date:'
sheet['A10'] = 'Contract'
sheet['B10'] = 'Scope'
# 
sheet['A14'] = 'ITEM'
sheet['C14'] = 'QTY'
sheet['D14'] = 'UNIT'
sheet['B10'] = 'PRICE'
sheet['E14'] = 'AMOUNT'
sheet['C22'] = 'SUBTOTAL'
sheet['E22'] = '=SUM(E15:E21)'
sheet['C23'] = 'TAX (%)'
sheet['C24'] = 'TAX'
sheet['E24'] = '=E22*E23'
sheet['C25'] = 'TOTAL'
sheet['D25'] = 'USD'
sheet['E25'] = '=SUM(A30:A31)'




# Invoice seller information
sheet['A1'] = json.dumps(sellerdata["seller"]["me"]["company"]).strip('"')
sheet['D1'] = json.dumps(sellerdata["seller"]["invoice"]["name"]).strip('"')
sheet['A22'] = json.dumps(sellerdata["seller"]["invoice"]["sweetmsg"]).strip('"')
sheet['A27'] = json.dumps(sellerdata["seller"]["invoice"]["footer"]).strip('"')
sheet['A28'] = json.dumps(sellerdata["seller"]["invoice"]["contactemail"]).strip('"')

# Invoice seller write
sheet['A3'] = json.dumps(sellerdata["seller"]["me"]["name"]).strip('"')
sheet['A4'] = json.dumps(sellerdata["seller"]["me"]["company"]).strip('"')
sheet['A5'] = json.dumps(sellerdata["seller"]["me"]["address"]).strip('"')
sheet['A6'] = json.dumps(sellerdata["seller"]["me"]["city"]).strip('"')
sheet['A7'] = json.dumps(sellerdata["seller"]["me"]["phone"]).strip('"')
sheet['A8'] = json.dumps(sellerdata["seller"]["me"]["mail"]).strip('"')

# Invoice client write
sheet['B3'] = json.dumps(clientdata["clients"]["SuperDuperClient"]["name"]).strip('"')
sheet['B4'] = json.dumps(clientdata["clients"]["SuperDuperClient"]["company"]).strip('"')
sheet['B5'] = json.dumps(clientdata["clients"]["SuperDuperClient"]["address"]).strip('"')
sheet['B6'] = json.dumps(clientdata["clients"]["SuperDuperClient"]["city"]).strip('"')
sheet['B7'] = json.dumps(clientdata["clients"]["SuperDuperClient"]["phone"]).strip('"')
sheet['B8'] = json.dumps(clientdata["clients"]["SuperDuperClient"]["mail"]).strip('"')
sheet['E3'] = '00001'
sheet['E4'] = datetoday
sheet['E5'] = datetoday
sheet['A11'] = json.dumps(clientdata["clients"]["SuperDuperClient"]["contract"]).strip('"')
sheet['B11'] = json.dumps(clientdata["clients"]["SuperDuperClient"]["scope"]).strip('"')

# (line 1) Invoice items and values 
sheet['A15'] = 'Automation Leadership' 
sheet['C15'] = '1'
sheet['D15'] = '1000'
sheet['E15'] = '1000'
# (line 2) 
sheet['A16'] = 'Cloud Architectture' 
sheet['C16'] = '1'
sheet['D16'] = '1000'
sheet['E16'] = '1000'




# Save populated file
xfile.save('invoice_' + datetodayout + '.xlsx')
