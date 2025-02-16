import json
import pyaudio
from vosk import Model, KaldiRecognizer

# Load Vosk Model
model = Model("../vosk-model-small-en-us-0.15")

# Configure microphone input
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000,
                input=True, frames_per_buffer=4000)
stream.start_stream()

# Initialize recognizer
rec = KaldiRecognizer(model, 16000)

print("🎤 Speak now... (Press CTRL+C to exit)")

try:
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())["text"]
            print("📝 Recognized:", result)

except KeyboardInterrupt:
    print("\n🛑 Stopped by user")
    stream.stop_stream()
    stream.close()
    p.terminate()
