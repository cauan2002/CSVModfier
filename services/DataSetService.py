import pandas as pd



class DataSetService:
    def __init__(self):
        return None

    def create_dataset(self, filepath):

         dados = pd.read_csv(filepath)
         return dados.head(5).to_html(classes='table table-bordered table-hover')
