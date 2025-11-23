from pydub import AudioSegment

audio=AudioSegment.from_file(r"G:\sem-3\python_lab\lab20\file_example_WAV_1MG.wav")
audio_fade_in=audio.fade_in(3000)
audio_fade_in.export(r'G:\sem-3\python_lab\lab20\audio_file_fade_in.wav',format='wav')
