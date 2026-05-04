FROM python:3.11-slim
WORKDIR /convertisseur
RUN pip install requests
COPY convertisseur.py .
CMD ["python", "convertisseur.py"]