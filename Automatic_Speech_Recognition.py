from transformers import pipeline

asr = pipeline("automatic-speech-recognition")

result = asr("audio.wav")

print(result)