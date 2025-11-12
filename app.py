import os
from flask import Flask, current_app
from openai import uploads    
from DownloadServices.DownloadHead import DownloadHead
from services.Uploadservice import UploadService

def create_app():
   app = Flask(__name__) 
   
   upload_folder= "uploads"
   app.config["UPLOAD_FOLDER"] = upload_folder
   app.secret_key = "secret"
   os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)



   from DownloadServices.DownloadHead import download_bp
   app.register_blueprint(download_bp)

   from services.Uploadservice import upload_blue
   app.register_blueprint(upload_blue)

  

   return app