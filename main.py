
import queue
import sounddevice as sd
import vosk
import sys
import json

from commands import parseCommand

q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

model = vosk.Model("/Users/ben/home/programming/personal/ai-assistent/vosk-model-small-de-0.15")  # Pfad zum entpackten Modell

with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                       channels=1, callback=callback):
    rec = vosk.KaldiRecognizer(model, 16000)
    print("Sprich jetzt...")

    while True:
        data = q.get()
        if rec.AcceptWaveform(data):
            result = rec.Result()
            text = json.loads(result).get("text", "")
            if text:
                if text == "exit":
                    break

                print("Erkannt:", text)

                parseCommand(text)
        else:
            partial_result = rec.PartialResult()
            partial_text = json.loads(partial_result).get("partial", "")
            if partial_text:
                print("Zwischenergebnis:", partial_text)


