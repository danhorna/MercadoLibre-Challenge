import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.errors import HttpError

# Nuestro peticiones podrian devolver diferentes codigos de errores HTTP.
# Como el challenge solo nos pide devolver un '404' lo hago de esta forma.
# Es posible extender esta funcionalidad dejando en claro cual es el error obtenido, se puede realizar con las siguientes lineas:
# ---------------------
# from googleapiclient.errors import HttpError
# import json
# except HttpError as e:
# error_reason = json.loads(e.content)
# ---------------------
# Entonces en error_reason tenemos desde el codigo de error HTTP, hasta el mensaje descriptivo.

class GoogleDrive():
    def __init__(self):
        SCOPES = ['https://www.googleapis.com/auth/drive']
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    './app/static/credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        self.service = build('drive', 'v3', credentials=creds)
    
    def word_in_doc(self, word, fileId):
        found = False
        try:
            results = self.service.files().list(q="fullText contains '{}'".format(word)).execute()
            files = results.get('files')
            for doc in files:
                if doc['id'] == fileId:
                    found = True
            return found
        except HttpError as e:
            # error_reason = json.loads(e.content)
            return found

    def file_exists_by_id(self, fileId):
        try:
            # Podemos ampliar la aplicacion devolviendo el archivo entregado con -return theFile
            theFile = self.service.files().get(fileId=fileId).execute()
            return True
        except HttpError as e:
            # error_reason = json.loads(e.content)
            return False

    def new_file(self, fileData):
        try:
            theFile = self.service.files().create(body=fileData, fields='id,name,description').execute()
            return theFile
        except HttpError as e:
            # error_reason = json.loads(e.content)
            return False