FROM python:3.9
ENV PYTHONUNBUFFERED 1
RUN mkdir /acs_cash
WORKDIR /acs_cash
COPY requirements.txt /acs_cash/
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /acs_cash/