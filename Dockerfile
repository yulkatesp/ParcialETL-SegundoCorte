# Usa Python 3.11 (ruedas manylinux disponibles para pandas 2.x)
FROM python:3.11-slim

# Evita prompts durante apt
ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

# Dependencias del sistema mínimas (no demasiado pesadas).
# Esto cubre situaciones donde paquetes necesitan headers básicos.
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements e instalar (upgrade pip para mejores ruedas)
COPY requirements.txt .
RUN python -m pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de la app
COPY . .

# Variable de puerto (Railway provee PORT en runtime)
ENV PORT=${PORT:-8000}

# Comando por defecto
CMD ["python", "main.py"]
