import os, json
import dict2xml
from dict2xml import dict2xml
from pyDes import *
import bz2
import boto3


# Parameters
json_dir = "jsons/"
xml_dir = "xmls/file.xml"
password = '12345678'
bucketName = "pythondockertask"
s3_file = "enc_file.xml"

# Read the JSON file from the JSON directory Convert to XML 
def convertjson2xml(json_dir):
    for file in os.listdir(json_dir):
        full_filename = "%s/%s" % (json_dir, file)
        with open(full_filename,'r') as fi:
            json_dict = json.load(fi)
            xml_files = dict2xml(json_dict, 'template')
            return xml_files

# Encrypt the XML file
def encrypt(xml_dir,password):
    k = des(password, CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
    d = k.encrypt(xml)
    return d

# Execute the above functiosn to convert and encrypt the file
xml = convertjson2xml(json_dir)
encrypted_data = encrypt(xml,password)

enc_file = open(xml_dir,'wb')
enc_file.write(encrypted_data)
enc_file.close()


# Upload the encrypted file to S3 bucket
s3 = boto3.resource('s3')
s3.meta.client.upload_file(xml_dir,bucketName,s3_file)
