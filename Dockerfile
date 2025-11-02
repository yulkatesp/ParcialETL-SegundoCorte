FROM python:latest
WORKDIR /app

# Copiar requerimientos e instalar
COPY requirements.txt .
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de la app
COPY . .

# Puerto (Railway proporcionará PORT)
ENV PORT=${PORT:-8000}

CMD ["python", "main.py"]
