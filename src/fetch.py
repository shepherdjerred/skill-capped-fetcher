import boto3
import requests
import re


def handler(event, context):
    page = requests.get('https://www.skill-capped.com/lol/browse')
    content = page.text
    url = re.search("loc: *\"(.*)\"", content).groups()[0]
    print(f"Found URL: {url}")

    json_page = requests.get(url)
    json_content = json_page.text

    s3 = boto3.resource('s3')
    s3Object = s3.Object('com.shepherdjerred.better-skill-capped',
                         'skill-capped-manifest.json')

    s3Object.put(Body=json_content)
