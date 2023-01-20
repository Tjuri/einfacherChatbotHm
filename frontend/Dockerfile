FROM python:3.8-buster AS BASE

RUN apt-get update && \
    apt-get --assume-yes --no-install-recommends install \
    build-essential \
    curl \
    git \
    jq \
    libgomp1 \
    vim

WORKDIR /app
RUN pip install --no-cache-dir --upgrade pip

RUN pip install rasa

# Copy actions folder to working directory
COPY ./actions /app/actions

ADD credentials.yml credentials.yml
ADD endpoints.yml endpoints.yml
ADD config.yml config.yml
ADD domain.yml domain.yml

EXPOSE 5005
CMD ["--help"]