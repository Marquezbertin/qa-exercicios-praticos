FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir matplotlib numpy

COPY artefatos/gerar_figuras.py .

RUN mkdir -p artefatos/figuras

CMD ["python", "gerar_figuras.py"]
