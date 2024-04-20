import os


class SpeechUtils:
    @staticmethod
    def say(text: str):
        os.system(f'say "{text}"')
