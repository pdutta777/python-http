FROM python:alpine3.6
COPY app /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV PORT 8080
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["app.py"]
