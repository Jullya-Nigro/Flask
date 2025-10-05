# Imagem
FROM python:3.12.10-slim

# Define diretório de trabalho
WORKDIR /app

# Copia o requirements.txt para instalar dependências
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código
COPY . .

# Porta que o Flask usa
EXPOSE 5002

# Para rodar a aplicação
CMD ["python", "app.py"]
