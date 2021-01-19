import json

def newfile_parameters(params):
    # En vez de recibir "titulo" y "descripcion" en el POST, hubiera estado bueno que sea "title" y "description" para ahorrarnos la creacion de fileData
    if 'titulo' not in params or 'descripcion' not in params:
        return False
    fileData = {
        "name": params['titulo'],
        "description": params['descripcion']
    }
    return fileData
