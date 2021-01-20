from flask import jsonify
from flask_restful import Resource, abort, request
from app.helpers.gdrive import GoogleDrive
from app.helpers.utils import newfile_parameters
gDrive = GoogleDrive()

class SearchInDoc(Resource):
    def get(self, id):
        word = request.args.get('word')
        if not word:
            abort(400, message="Parameter 'word' required")
        fileExist = gDrive.file_exists_by_id(id)
        # Se podria poner fileExist y wordInDoc en el mismo condicional, pero no seria idóneo, ya que de no existir el archivo, haria una request innecesaria.
        if not fileExist:
            abort(404, message="File not found")
        wordInDoc = gDrive.word_in_doc(word,id)
        if not wordInDoc:
            abort(404, message="Word not found")
        return jsonify({
            "message": "Word found in Doc!"
        })

class NewFile(Resource):
    def post(self):
        data = request.get_json()
        fileData = newfile_parameters(data)
        if not fileData:
            abort(400, message="Bad parameters")
        fileCreated = gDrive.new_file(fileData)
        if not fileCreated:
            abort(500)
        # Al igual que en newfile_parameters(), hubiera estado bueno que la respuesta a entregar sea id-name-description y no id-titulo-descripcion
        # Así podriamos hacer simplemente el return de fileCreated. 
        return jsonify({
            "id": fileCreated['id'],
            "titulo": fileCreated['name'],
            "descripcion": fileCreated['description']
        })