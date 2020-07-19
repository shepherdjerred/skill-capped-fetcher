import boto3
import requests
import re

def handler(event, context):
    page = requests.get('https://www.skill-capped.com/lol/browse')
    content = page.text
    print(f"Content: {content}")
    url = re.search("loc: *\"(.*)\"", content).groups()[0]
    print(f"Found URL: {url}")

    jsonPage = requests.get(url)
    jsonContent = jsonPage.text
    print(f"JSON content: {jsonContent}")
    binaryContent = ' '.join(format(ord(x), 'b') for x in jsonContent)
    print(f"Binary content: {binaryContent}")

    s3 = boto3.resource('s3')
    s3Object = s3.Object('com.shepherdjerred.better-skill-capped', 'skill-capped-manifest.json')
    s3Object.put(Body=jsonContent)
