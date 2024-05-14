# To build docker build -t webapp:1.0 .
# To run docker run -d -p 80:5000 --name web webapp:1.0
FROM python:3.10.0-alpine3.15
WORKDIR /app
COPY requirement.txt .
RUN pip3 install -r requirement.txt
COPY src src
EXPOSE 5000
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
            CMD curl -f http://localhost:5000/health || exit 1
ENTRYPOINT ["python", "./src/app.py"]