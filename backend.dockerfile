FROM python:3.12-alpine

WORKDIR /app

COPY . .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    chmod +x backend.entrypoint.sh && \
    apk add --no-cache postgresql-client

EXPOSE 8000

ENTRYPOINT ["./backend.entrypoint.sh"]