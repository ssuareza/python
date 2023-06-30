FROM python:3.10-slim

ENV PATH $PATH:/root/.local/bin

WORKDIR /app

# base dependencies
RUN apt-get update && apt-get -y --no-install-recommends install \
  entr \
  g++ \
  gcc \
  git \
  libicu-dev \
  libtk8.6 \
  make \
  pkg-config \
  && rm -rf /var/lib/apt/lists/*

# python dependencies
COPY grammar/requirements.txt ./
RUN pip install torch==2.0.1 --extra-index-url https://download.pytorch.org/whl/torch_stable.html
RUN pip install -r ./requirements.txt

# download english model
RUN python3 -m spacy download en

CMD ["/app/bin/boot.sh"]
# CMD ["tail", "-f", "/dev/null"]
