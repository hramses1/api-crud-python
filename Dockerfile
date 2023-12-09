# Usa una imagen oficial de Python como imagen base
FROM python:3.11-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos 'requirements.txt' y los instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código fuente de tu aplicación al directorio de trabajo
COPY . .

# Informa a Docker que la aplicación se ejecuta en el puerto 8000
EXPOSE 8000

# Usa Uvicorn para ejecutar la aplicación
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
