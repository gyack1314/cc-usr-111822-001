FROM python:3.11-slim
WORKDIR /app
COPY . .
CMD ["python","-m","panel_ops.cli","data/example.json"]
