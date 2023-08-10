FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Copy project
COPY . /app/

# Run server
CMD python manage.py runserver 0.0.0.0:8000
