from flask import Flask, app, request, jsonify, session, Blueprint, current_app
from .DataSetService import DataSetService
import os


upload_blue = Blueprint('upload',__name__)


class UploadService:
    def __init__(self):
        
        return None
    

    def upload(self):
        file = request.files['file']
        if file and file.filename.endswith('.csv'):
            filepath = os.path.join(current_app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)

            session['uploaded_file'] = file.filename
             

            preview_html = DataSetService().create_dataset(filepath)

            return jsonify({"status":"ok",
                    "message": f"arquivo{file.filename} enviado com sucesso",
                    "preview_html": preview_html})
        else:
            return jsonify({"status":"erro",
                            "message":"formato de aquivo invalido, enivie um aqrquivo '.csv' "}),400



if __name__=="__main__":
    current_app.run(debug=True)
    current_app.secret_key = "secret_key"
