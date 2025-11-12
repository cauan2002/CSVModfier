from flask import Flask, request, jsonify, render_template
from services.Uploadservice import UploadService
from DownloadServices import DownloadHead as dh
import os
from app import create_app


app = create_app()

class main:
    def __init__(self):
       print("iniciando app")
    

    @app.route('/')
    def tela_inicial():
        return render_template('index.html')
    

    @app.route('/upload', methods=['POST'])
    def upload_file():

        return UploadService().upload()
    
    @app.route('/download_head', methods=['GET'])
    def download_head():
        return dh.DownloadHead().Download_head(request.args.get('filename'))
    
    @app.route('/download_tail', methods = ['GET'])
    def download_tail():
        return dh.DownloadHead().Download_tail(request.args.get('filename'))
    

    @app.route('/filtrar_csv', methods = ['POST'])
    def filtrar_csv():
        return dh.DownloadHead().download_Filter(request.args.get('filename'))

    



    
if __name__=="__main__":
    main()
    app.run(debug=True)
  

    