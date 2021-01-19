from flask import jsonify
from flask_restful import Resource, abort, request
from app.helpers.gdrive import GoogleDrive

class SearchInDoc(Resource):
    def get(self, id):
        gDrive = GoogleDrive()
        word = request.args.get('word')
        fileExist = gDrive.file_exists_by_id(id)
        if not word:
            abort(400, message="Parameter 'word' required")
        # Se podria poner fileExist y wordInDoc en el mismo condicional, pero no seria idóneo, ya que de no existir el archivo, haria una request innecesaria.
        if not fileExist:
            abort(404, message="File not found")
        wordInDoc = gDrive.word_in_doc(word,id)
        if not wordInDoc:
            abort(404, message="Word not found")
        return jsonify({
            "message": "Word found in Doc!"
        })