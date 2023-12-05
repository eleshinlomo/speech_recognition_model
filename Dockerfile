FROM python:3.11-slim

WORKDIR /app

COPY . /app

COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip && \
    python3 -m pip install --upgrade setuptools && \
    python3 -m pip install --no-cache-dir -r requirements.txt
    
    

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]