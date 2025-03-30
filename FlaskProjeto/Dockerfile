# Use a imagem oficial do Python 3.12 slim como base
FROM python:3.12-slim

# Instalar dependências do sistema para compilar pacotes
RUN apt-get update && apt-get install -y curl && apt-get clean && rm -rf /var/lib/apt/lists/*

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo requirements.txt para o contêiner
COPY requirements.txt ./

# Instala as dependências utilizando pip
RUN pip install --no-cache-dir -r requirements.txt

# Define a variável de ambiente
ENV FILE_PATH_DB_MOVEIS="/app/filmes.db"

# Copia o restante dos arquivos para o contêiner
COPY . .

# Expondo a porta que a aplicação irá rodar
EXPOSE 8050

# Comando para rodar a aplicação
CMD ["python", "app.py"]
