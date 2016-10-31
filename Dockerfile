FROM django

MAINTAINER laurent loukopoulos <laurent.loukopoulos@gmail.com>

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
            postgresql-client \
	        && rm -rf /var/lib/apt/lists/*

RUN mkdir laurent
RUN mkdir laurent/app

WORKDIR /home/laurent/app
COPY urbit/. .

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]