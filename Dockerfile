FROM alpine:3.13.12
COPY . /app
WORKDIR /app
RUN apk add python3 py3-pip && pip3 install openpyxl xlsxwriter boto3
ENTRYPOINT ["python3", "./invoice-generator.py"]
#
# docker run -it -v $PWD:/app invoce-generator me foocha e
