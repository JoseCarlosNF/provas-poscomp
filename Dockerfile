FROM python:3.9.7-alpine3.14 as dev
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]

FROM public.ecr.aws/lambda/python:3.9 as prod
COPY provas_poscomp .
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
CMD ["main.handler"]
