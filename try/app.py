"""import speech_to_text

# Create a client object.
client = speech_to_text.SpeechToTextClient()

# Start listening for audio.
stream = client.start_streaming(
    microphone=True,
    language_code='en-US'
)

# Transcribe the audio as it is being recorded.
while True:
    result = stream.read()
    if result.error:
        print(result.error)
        break
    print(result.alternatives[0].transcript)"""
from google.cloud import texttospeech

# Instantiates a client
client = texttospeech.TextToSpeechClient()

# Set the text input to be synthesized
synthesis_input = texttospeech.SynthesisInput(text="Hello, world!")

# Build the voice request
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

# The response's audio_content is binary.
with open("output.mp3", "wb") as out:
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')

