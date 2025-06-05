
FROM python:3.7.7 as builder

WORKDIR /app

COPY requirements.txt .

RUN python -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.7.7-slim

WORKDIR /app

COPY --from=builder /opt/venv /opt/venv

COPY . .

ENV PATH="/opt/venv/bin:$PATH"

EXPOSE 5000

ENV FLASK_APP=application.py
ENV FLASK_ENV=production

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
