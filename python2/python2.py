import os, json
import dict2xml
from dict2xml import dict2xml
from pyDes import *
import bz2
import boto3

# Parameters

xml_dir = "xmls/file.xml"
password = '12345678'
bucketName = "pythondockertask"
s3_file = "enc_file.xml"

# The decryption function
def decrypt(data,password):
    k = des(password, CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
    d = k.decrypt(data)
    return d

# Download the encrypted file from S3 bucket
s3 = boto3.resource('s3')
try:
    s3.Bucket(bucketName).download_file(s3_file, xml_dir)
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise

# Execute the above function to decrypt the file and store it
enc_file = open(xml_dir,'rb')
decrypted_data = decrypt(enc_file.read(),password)

decrypted_file = open(xml_dir,'wb')
decrypted_file.write(decrypted_data)
decrypted_file.close()