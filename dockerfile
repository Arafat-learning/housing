FROM python:3.12-slim

WORKDIR /app

# Install system dependencies needed for Scrapy
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libxml2-dev \
    libxslt-dev \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Scrapy
RUN pip install scrapy

# Install script
COPY install_requirements.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/install_requirements.sh

CMD ["/usr/local/bin/install_requirements.sh"]
