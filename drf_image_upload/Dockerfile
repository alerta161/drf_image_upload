FROM python:3.10
    ENV PYTHONUNBUFFERED 1
    RUN mkdir /drf_image_upload
    WORKDIR /drf_image_upload
    ADD requirements.txt /drf_image_upload/
    RUN pip install -r requirements.txt
    ADD . /drf_image_upload/