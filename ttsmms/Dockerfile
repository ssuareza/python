FROM python:3.10-slim

ENV PATH $PATH:/root/.local/bin

WORKDIR /app

# base dependencies
RUN apt-get update; \
  apt-get install -y --no-install-recommends \
  entr \
  make \
  gcc \
  ; \
  rm -rf /var/lib/apt/lists/*

# python dependencies
COPY ttsmms/requirements.txt ./
RUN pip install torch==2.0.1 --extra-index-url https://download.pytorch.org/whl/torch_stable.html
RUN pip install torchvision==0.15.2 --extra-index-url https://download.pytorch.org/whl/torch_stable.html
RUN pip install -r ./requirements.txt

CMD ["/app/bin/boot.sh"]
