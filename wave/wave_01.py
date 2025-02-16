import wave

obj = wave.open('../file/record_out.wav', 'rb')

print('Number of Channels',obj.getnchannels())
print('Sample width',obj.getsampwidth())
print('Frame rate', obj.getframerate())
print('Number of frames', obj.getnframes())
print('parameters', obj.getparams())

# len of audio
t_audio  = obj.getnframes() / obj.getframerate()
samp_width = obj.getsampwidth()

print(t_audio)
frames = obj.readframes(-1)
print(type(frames), type(frames[0]))
print(len(frames))
obj.close()

obj_new = wave.open('../file/record_out_2.wav', 'wb')
obj_new.setnchannels(obj.getnchannels())
obj_new.setsampwidth(obj.getsampwidth())
obj_new.setframerate(obj.getframerate())

reversed_frames = bytearray()
# for i in range(0, len(frames), samp_width):
#     reversed_frames[:0] = frames[i:i + samp_width]

obj_new.writeframes(frames)
obj_new.close()

