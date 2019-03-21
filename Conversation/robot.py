from text_to_speech import TextToSpeech
from chatting import Chat
from sound_rec_demo import SpeechToText
from datetime import datetime

while True:
    flag = True
    while flag:
        try:
            speaking = SpeechToText()
            start_speechtotext = datetime.now()
            input_sentence = SpeechToText().record_to_file()
            end_speechtotext = datetime.now()
            print(input_sentence)
            start_chat = datetime.now()
            response = Chat(input_sentence).convert()
            end_chat = datetime.now()
            voice = TextToSpeech()
            start_voice = datetime.now()
            print('response: ', response)
            voice.play(voice.get_audio_bytes(response))
            end_voice = datetime.now()
            #print('Speech to Text: ', (end_speechtotext - start_speechtotext).seconds)
            #print('Chatting Bot: ', (end_chat - start_chat).seconds)
            #print('Text to Speech: ', (end_voice - start_voice).seconds)
        except:
            voice = TextToSpeech()
            voice.play(voice.get_audio_bytes("Sorry, I don't understand."))