# Imagem base Python 3.13
FROM python:3.13-slim

# Instala dependências do sistema necessárias para o mysqlclient
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    gcc \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Define a pasta de trabalho
WORKDIR /app

# Copia e instala as dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o projeto
COPY . .

# Expõe a porta
EXPOSE 8000

# Roda o servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]