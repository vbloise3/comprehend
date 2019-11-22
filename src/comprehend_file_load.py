import sys
import boto3
import json


def read_file(file_name):
    contents = ''
    f = open(file_name, "r")
    if f.mode == 'r':
        contents += f.read()
    f.close()
    comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')
    print(json.dumps(comprehend.detect_sentiment(Text=contents, LanguageCode='en'), sort_keys=True, indent=4))


if __name__ == '__main__':
    read_file(*sys.argv[1:])
