FROM python:3.12-slim
WORKDIR /app
COPY exporter ./exporter
RUN pip install prometheus-client
EXPOSE 9100
CMD ["python", "exporter/main.py"]
