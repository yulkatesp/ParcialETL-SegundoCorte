# Imagen base con Python más reciente
FROM python:latest

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar archivo de dependencias
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY . .

# Comando por defecto para ejecutar tu script
CMD ["python", "main.py"]
