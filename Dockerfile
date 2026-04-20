# ── Etapa 1: imagen base ligera ──────────────────────────────────────────────
FROM python:3.11-slim

# Metadatos de la imagen
LABEL maintainer="tu-usuario@email.com"
LABEL description="App Hola Mundo - Práctica DevOps"
LABEL version="1.0"

# Variables de entorno: evita archivos .pyc y activa logs en tiempo real
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    FLASK_ENV=production

# ── Directorio de trabajo dentro del contenedor ───────────────────────────────
WORKDIR /app

# ── Instalar dependencias (primero para aprovechar la caché de Docker) ────────
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ── Copiar el código fuente ───────────────────────────────────────────────────
COPY app.py .

# ── Puerto que expone la aplicación ──────────────────────────────────────────
EXPOSE 5000

# ── Comando de inicio con Gunicorn (servidor WSGI para producción) ────────────
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:app"]
