# Usa a imagem base do Python
FROM python:3.9

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia apenas o arquivo de requisitos para o container
COPY requirements.txt .

# Instala as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia os arquivos de código para o container
COPY . .

# Exponha a porta em que a aplicação Flask será executada
EXPOSE 5000

# Define variáveis de ambiente para Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development

# Comando padrão para executar a aplicação Flask
CMD ["flask", "run"]
