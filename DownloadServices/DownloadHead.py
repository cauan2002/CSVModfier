
from flask import  Flask, app, current_app, request, jsonify, send_file, session, Blueprint
from services.Uploadservice import UploadService
from services.DataSetService import DataSetService  
import pandas as pd
import os

download_bp = Blueprint('download', __name__)


class DownloadHead:
    def __init__(self):
        return None
    
    def Download_head(self,filename):
        filename = session.get('uploaded_file')

        if not filename:
            return "nenhum arquivo enviado",400

        filepath = os.path.join(current_app.config["UPLOAD_FOLDER"], filename)


        if    not os.path.exists(filepath):
            return 'arquivo nao encontrado no diretorio', 400


        df_head = pd.read_csv(filepath).head(10)
        temp_filepath = os.path.join(current_app.config["UPLOAD_FOLDER"], 'head_' + filename)
        df_head.to_csv(temp_filepath, index=False)

        return send_file(temp_filepath, as_attachment=True)
    

    def Download_tail(self, filename):
         filename = session.get('uploaded_file')

         if not filename:
            return "nenhum arquivo enviado",400

         filepath = os.path.join(current_app.config["UPLOAD_FOLDER"], filename)


         if    not os.path.exists(filepath):
            return 'arquivo nao encontrado no diretorio', 400


         df_head = pd.read_csv(filepath).tail(10)
         temp_filepath = os.path.join(current_app.config["UPLOAD_FOLDER"], 'tail_' + filename)
         df_head.to_csv(temp_filepath, index=False)

         return send_file(temp_filepath, as_attachment=True)
        


    def  download_Filter(self,filename):   
        filename = session.get('uploaded_file')
         
        if not filename:
            return "nunhum arquivo enviado",400
        
        filepath = os.path.join(current_app.config["UPLOAD_FOLDER"], filename)

        if    not os.path.exists(filepath):
            return 'arquivo nao encontrado no diretorio', 400
        
        colunas = request.form.get("coluna")
        valor = request.form.get("valor")

        if colunas and valor:
            colunas = [c.strip() for c in colunas.split(',')]
            valor =   [ v.strip() for v in valor.split(',')]

        else: 
            return "parametros invalidos",400   
        
        df = pd.read_csv(filepath)
        df_filtered = df

        temp_filepath = os.path.join(current_app.config["UPLOAD_FOLDER"], 'filtered_' + filename)
        df_filtered.to_csv(temp_filepath, index=False)


        for c, v in zip(colunas, valor):
            if c in df.columns:
                df_filtered = df_filtered[df_filtered[c]==v]

        temp_filepath = os.path.join(current_app.config["UPLOAD_FOLDER"], 'filtered_' + filename)
        df_filtered.to_csv(temp_filepath, index=False, sep=';')        

        return send_file(temp_filepath, as_attachment=True)
    
     



      
            


