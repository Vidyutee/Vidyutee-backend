FROM python:3.9-slim

COPY . ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 80

# Run command
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]