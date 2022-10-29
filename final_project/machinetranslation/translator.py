import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv
load_dotenv()
apikey = os.environ['D_2vPC1hoblff0hBD-kcL5gSh4hdiFtnaFiX4H86g3ZF']
url = os.environ['https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/b8200348-4dbc-46fe-8e5f-3be41b415ef0']

auth = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version='{version}', authenticator= auth)
language_translator.set_service_url(url)


def englishToFrench(englishText):
    frenchText = translate_text(englishText, 'en', 'fr')
    return frenchText

def frenchToEnglish(frenchText):
    english_Text = translate_text(frenchText, 'fr', 'en')
    return english_Text