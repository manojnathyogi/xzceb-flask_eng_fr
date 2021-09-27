from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

URL = 'https://api.us-south.language-translator.watson.cloud.ibm.com/instances/971ca9f6-ea42-4f03-86bd-f290c32de433'
APIKEY = '_wETvMMpcZVt0YObpse2_jToi-pE07zyfP0CBDsfkAQe'
VERSION = '2018-05-01'
authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(version = VERSION, authenticator = authenticator)
language_translator.set_service_url(URL)

def eng_french(eng_text):
    '''Translates english text to french'''
    french_translation = language_translator.translate(text = eng_text,
    model_id = 'en-fr').get_result()
    translation = french_translation['translations'][0]['translation']
    return translation

def french_eng(french_text):
    '''Translates french text to english '''
    english_translation = language_translator.translate(text = french_text,
    model_id = 'fr-en').get_result()
    translation = english_translation['translations'][0]['translation']
    return translation
