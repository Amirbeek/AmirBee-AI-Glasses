from pydub import AudioSegment

audio = AudioSegment.from_wav("../file/record_out.wav")

audio = audio + 6
audio = audio * 2

audio = audio.fade_in(2000)

audio.export("../file/record_out.mp3", format="mp3")


audio2 = AudioSegment.from_mp3("../file/record_out.mp3")
print('done')