# 🧾 **CSV Modifier – Sistema Web para Upload e Processamento de Arquivos CSV**

## 📖 **Descrição do Projeto**

O **CSV Modifier** é uma aplicação web desenvolvida em **Python com Flask**, criada para **upload, filtragem e download de arquivos CSV** de forma simples e intuitiva.  
O sistema permite enviar arquivos, processar seus cabeçalhos ou partes específicas e baixar os resultados filtrados automaticamente.

---

## ⚙️ **Tecnologias Utilizadas**

- 🐍 **Python 3.x**  
- 🌐 **Flask** (framework web)  
- 📦 **Werkzeug** (upload de arquivos)  
- 💾 **OS e manipulação de diretórios**  
- 🧩 **Serviços e Blueprints** para modularidade da aplicação
---

## 🧱 **Estrutura do Projeto**

csvmodifier/
│

├── app.py # Criação e configuração principal do Flask
├── main.py # Ponto de entrada da aplicação (rotas e inicialização)
│

├── services/

│ └── Uploadservice.py # Lógica de upload dos arquivos CSV
│

├── DownloadServices/
│ └── DownloadHead.py # Funções para download, filtragem e cabeçalho dos CSVs
│


├── uploads/ # Pasta onde os arquivos enviados são armazenados
│


├── templates/
│ └── index.html # Interface HTML para upload e manipulação
│


└── README.md # Documentação do projeto



🌐 Rotas Principais

Rota	Método	Descrição
/	GET	Exibe a página inicial (upload de CSV)

/upload	POST	Faz o upload do arquivo CSV

/download_head	GET	Faz o download apenas do cabeçalho do arquivo CSV

/download_tail	GET	Faz o download das últimas linhas do arquivo CSV

/filtrar_csv	POST	Permite filtrar o conteúdo de um CSV conforme os parâmetros definidos



🧠 Conceitos-Chave do Projeto

Modularização com Blueprints: cada serviço (upload, download) é independente.

Persistência temporária de arquivos: os CSVs são salvos em uploads/.

Separação de responsabilidades:

app.py → configuração base do Flask.

main.py → rotas e controle da aplicação.

services/ e DownloadServices/ → lógica de negócio.



🧩 Melhorias Futuras

melhoria na arquitetura do projeto, usando paradigmas mais solidos e arquitetura limpa

Adicionar interface mais moderna (HTML + CSS/Bootstrap).

Implementar autenticação para uploads privados.

Adicionar logs e tratamento de erros detalhados.

Permitir download de arquivos filtrados em formatos diferentes (CSV, Excel).


👨‍💻 Autor

Jardeson Cauã

📍 Fortaleza - CE

📧 cauanjardeson@gmail.com

