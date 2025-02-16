import os
import assemblyai as aai

API_KEY = "f11ea6dd38ad47d9b30b8f9ecc917983"

# Set the API key for AssemblyAI
aai.settings.api_key = API_KEY

transcriber = aai.Transcriber()

audio_file = "../../file/record_out.wav"

# ✅ Check if file exists before proceeding
if not os.path.exists(audio_file):
    print(f"❌ Error: Audio file not found at {audio_file}")
    exit(1)

# Configure transcription settings
config = aai.TranscriptionConfig(speaker_labels=True)

# 📝 Start transcription
try:
    transcript = transcriber.transcribe(audio_file, config)

    # ✅ Check if the transcription succeeded
    if transcript.status == aai.TranscriptStatus.error:
        print(f"❌ Transcription failed: {transcript.error}")
        exit(1)

    # 🎤 Print the full transcription
    print("\n🎧 **Transcription Output:**")
    print(transcript.text)

    # 🗣️ Print speaker-labeled segments
    print("\n🗣️ **Speaker Breakdown:**")
    for utterance in transcript.utterances:
        print(f"Speaker {utterance.speaker}: {utterance.text}")

except Exception as e:
    print(f"⚠️ Error during transcription: {e}")
