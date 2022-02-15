import speech_recognition as sr
import moviepy.editor as mp
from pathlib import Path
import os

def google_transfer(wavFilePath):
    try:
        r = sr.Recognizer()
        audio = sr.AudioFile(wavFilePath+'.wav')
        with audio as source:
            audio_file = r.record(source)
        result = r.recognize_google(audio_file,language = 'zh', show_all=True)
        transcripts = result['alternative']
        print(transcripts)
        # exporting the result
        with open(wavFilePath+'.txt', mode='w') as file:
            file.write("Recognized Speech:")
            file.write("\n")
            for item in transcripts:
                transcript = item['transcript']
                file.write("\n")
                file.write(transcript)
            file.write("\n")
            print("ready!")
    except:
        print('An exception occurred')


if __name__ == '__main__':
    d = "C:\\Users\\wuxig\\PycharmProjects\\TelegramBot\\audios"
    for path in os.listdir(d):
        full_path = os.path.join(d, path)
        for file_path in os.listdir(full_path):
            filename, file_extension = os.path.splitext(file_path)
            if file_extension == '.wav':
                filepath = os.path.join(full_path, filename)
                print(filepath)
                google_transfer(filepath)




