# Pull Base Image
FROM python

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# Work Directory
WORKDIR /app

# Install Requirements
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy Project
COPY . ./app

# VOLUME [ "/data" ]

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000