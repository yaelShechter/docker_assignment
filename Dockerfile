FROM python:3.9.5-slim-buster
WORKDIR /assignment
COPY . .
RUN apt update && yes | apt install toilet
CMD ["python", "fib.py"]
