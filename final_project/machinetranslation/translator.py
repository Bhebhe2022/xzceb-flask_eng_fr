"""System modules."""
from http import server
import json
import os
from xmlrpc.client import Server
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
from flask import Flask, render_template, request
load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com')

def english_to_french(english_text):
    """
    This function translates english to french
    """
    textToTranslate = request.args.get('textToTranslate')
    french_text = language_translator.translate(
        text=textToTranslate,
        model_id='en-fr').get_result()
    print(json.dumps(french_text, indent=2,
    ensure_ascii=False))
    return french_text

def french_to_english(french_text):

    """
    This function translates french to english
    """
    textToTranslate = request.args.get('textToTranslate')
    english_text = language_translator.translate(
        text=textToTranslate,
        model_id='fr-en').get_result()
    print(json.dumps(english_text, indent=2,
    ensure_ascii=False))
    return english_text