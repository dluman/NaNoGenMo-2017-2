import os

from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

folder = "CLEAR_WAV"

files = sorted(os.listdir('audio/'+folder))
gcs_uri = "gs://" + os.environ['GOOGLE_AUDIO_BUCKET'] + "/" + folder

for file in files:
	next_uri = gcs_uri + "/" + file
	client = speech.SpeechClient()
	audio = types.RecognitionAudio(uri=next_uri)
	config = types.RecognitionConfig(
		encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        	sample_rate_hertz=11025,
        	language_code='en-US')
	print "RUNNING " + next_uri
	operation = client.long_running_recognize(config, audio)
	try:
		response = operation.result(timeout=10000)
		for result in response.results:
			with open('transcript.txt','a') as f:
				f.write(format(result.alternatives[0].transcript)+ "\r\n")
	except:
		#TO-DO: WRITE MORE SPECIFIC ERROR HANDLING CODE
		print "ERROR? MOVING ON..."
