#!/usr/bin/python3
import urllib.request
import openpyxl
from datetime import date  
import json
import sys
import boto3
from botocore.exceptions import NoCredentialsError
import requests

# Uncomment it if you prefere use #
# ./invoice-generator.py me SuperDuperClient
get_seller=str(sys.argv[1])
get_client=str(sys.argv[2])
inv_type=str(sys.argv[3].lower()) # use always lower words

# If you use github actions you can replace it by github secrets ;) 
# It will be fixed later
ACCESS_KEY = 'XXXXXXXXXXXXXXXXXX'
SECRET_KEY = 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'
BUCKET_NAME= 'my-invoices'


# If you create bucket, remember use bucket policy. Example on s3_Bucket_policy.json
def upload_to_aws(local_file):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    try:
        s3.upload_file(str(local_file), BUCKET_NAME, str(local_file) ) 
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("Error in file")
        return False
    except NoCredentialsError:
        print("Error AWS S3 Credentials")
        return False
    # Send to S3 bucket (Optional)
    upload_to_aws('invoice_' + datetodayout + '.xlsx')


# Uncomment if prefere read local sellers file
#sellerfile = open('seller.json',)
#sellerdata = json.load(sellerfile)
#sellerfile.close()

# Uncomment if prefere read local clients file
#clientsfile = open('clients.json',)
#clientdata = json.load(clientsfile)
#clientsfile.close()
    
with urllib.request.urlopen("https://raw.githubusercontent.com/jpradoar/invoice_generator/main/seller.json") as url:
	sellerdata = json.load(url)

with urllib.request.urlopen("https://raw.githubusercontent.com/jpradoar/invoice_generator/main/clients.json") as url:
	clientdata = json.load(url)

# Generate data strings
getDate = date.today() 
datetoday = str(getDate.month)+ "/" + str(getDate.day) + "/" + str(getDate.year)   
datetodayout = str(getDate.month)+ "-" + str(getDate.day) + "-" + str(getDate.year)   

# Download last version of template
#URL = "https://github.com/jpradoar/invoice_generator/raw/main/template.xlsx"
#response = requests.get(URL)
#open("template.xlsx", "wb").write(response.content)

# Read Excel (or any xls)
xfile = openpyxl.load_workbook("template.xlsx")

#---------------------------
# Populate data :D 
#---------------------------

def a_invoice():
    print("Invoice type A")
    # Read tab/sheet of Excel doc (or any xls)
    sheet = xfile["Invoice_a"]

def b_invoice():
    print("Invoice type B")
    # Read tab/sheet of Excel doc (or any xls)
    sheet = xfile["Invoice_b"]

def c_invoice():
    print("Invoice type C")
    # Read tab/sheet of Excel doc (or any xls)
    sheet = xfile["Invoice_c"]        


def x_invoice():
    print("Invoice type x")
    # Read tab/sheet of Excel doc (or any xls)
    sheet = xfile["Invoice_x"]


def e_invoice():
    print("Invoice type E")
    # Read tab/sheet of Excel doc (or any xls)
    sheet = xfile["Invoice_e"]

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
    sheet['A1'] = json.dumps(sellerdata["seller"][get_seller]["company"]).strip('"')
    sheet['C1'] = json.dumps(sellerdata["seller"]["invoice"]["name"]).strip('"')
    sheet['A22'] = json.dumps(sellerdata["seller"]["invoice"]["sweetmsg"]).strip('"')
    sheet['A27'] = json.dumps(sellerdata["seller"]["invoice"]["footer"]).strip('"')
    sheet['A28'] = json.dumps(sellerdata["seller"]["invoice"]["contactemail"]).strip('"')

    # Invoice seller write
    sheet['A3'] = json.dumps(sellerdata["seller"][get_seller]["name"]).strip('"')
    sheet['A4'] = json.dumps(sellerdata["seller"][get_seller]["company"]).strip('"')
    sheet['A5'] = json.dumps(sellerdata["seller"][get_seller]["address"]).strip('"')
    sheet['A6'] = json.dumps(sellerdata["seller"][get_seller]["city"]).strip('"')
    sheet['A7'] = json.dumps(sellerdata["seller"][get_seller]["phone"]).strip('"')
    sheet['A8'] = json.dumps(sellerdata["seller"][get_seller]["mail"]).strip('"')

    # Invoice client write
    sheet['B3'] = json.dumps(clientdata["clients"][get_client]["name"]).strip('"')
    sheet['B4'] = json.dumps(clientdata["clients"][get_client]["company"]).strip('"')
    sheet['B5'] = json.dumps(clientdata["clients"][get_client]["address"]).strip('"')
    sheet['B6'] = json.dumps(clientdata["clients"][get_client]["city"]).strip('"')
    sheet['B7'] = json.dumps(clientdata["clients"][get_client]["phone"]).strip('"')
    sheet['B8'] = json.dumps(clientdata["clients"][get_client]["mail"]).strip('"')
    sheet['E3'] = '00001'
    sheet['E4'] = datetoday
    sheet['E5'] = datetoday
    sheet['A11'] = json.dumps(clientdata["clients"][get_client]["contract"]).strip('"')
    sheet['B11'] = json.dumps(clientdata["clients"][get_client]["scope"]).strip('"') 

    # PENDIG TO RESOLVE IT....
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



def invoice_type(inv_type):
    if inv_type == "a":
        a_invoice()
    elif inv_type == "b":
        b_invoice()
    elif inv_type == "c":
        c_invoice()
    elif inv_type == "x":
        x_invoice()
    elif inv_type == "e":
        e_invoice()
    else:
        print("Sorry: I cant create Invoice type: [" + inv_type + "]")





# Generate invoice type
invoice_type(inv_type)
# Save populated file
xfile.save('invoice_' + datetodayout + '.xlsx')

# Generate PDF (...PENDING)
#GoPDF('invoice_' + datetodayout + '.xlsx')

# Send to AWS S3
#upload_to_aws(local_file)