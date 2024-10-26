FROM python:3.12-slim

RUN apt-get update && apt-get install -y build-essential libpq-dev

WORKDIR /app

COPY ./requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . ./
RUN chmod +x /app/scripts/wait-for-it.sh

EXPOSE 8000

CMD ["/app/scripts/wait-for-it.sh", "probihy_db_container:5432", "--", "python", "manage.py", "runserver", "0.0.0.0:8000"]

# CMD ["npm", "start"]
