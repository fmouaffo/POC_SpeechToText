
import ModuleInstaller as mi

try:
    import boto3
except:
    mi.installModule("boto3")
    import boto3

import time
import urllib
import json
import datetime

AWS_ACCESS_KEY_ID = 'YourAccessKeyID'
AWS_SECRET_ACCESS_KEY = 'YourSecretAccessKey'

job_name = f"myFirstJobTranscribeFlo2-{datetime.datetime.now().timestamp()}"
job_uri = 'https://my-bucket-fms-1.s3.eu-west-3.amazonaws.com/folder1/test1.mp3'

myTranscribe = boto3.client('transcribe', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY, region_name='eu-west-3')

myTranscribe.start_transcription_job(TranscriptionJobName=job_name, Media={'MediaFileUri': job_uri}, MediaFormat='mp3', LanguageCode='fr-FR')

while True:
    myStatus = myTranscribe.get_transcription_job(TranscriptionJobName=job_name)
    if myStatus['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
        break
    print("Not ready yet...")
    time.sleep(4)
print(myStatus)

#if status['TranscriptionJob']['TranscriptionJobStatus'] == 'COMPLETED':
#    response = urllib.urlopen(status['TranscriptionJob']['Transcript']['TranscriptFileUri'])
#    data = json.loads(response.read())
#    text = data['results']['transcripts'][0]['transcript']
#    print(text)
