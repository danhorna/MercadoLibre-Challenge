from flask_restful import Resource
from app.helpers.gdrive import GoogleDrive

class SearchInDoc(Resource):
    def get(self):
        gDrive = GoogleDrive()
        print(gDrive.all_files())
