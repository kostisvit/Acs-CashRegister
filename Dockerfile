FROM python:3.9
ENV PATH="/scripts:${PATH}"
# Diasbles generation of pyc files
ENV PYTHONDONTWRITEBYTECODE 1
RUN mkdir /acs_cash
WORKDIR /acs_cash
COPY requirements.txt /acs_cash/
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /acs_cash/
RUN mkdir -p /vol/acs_cash/media
RUN mkdir -p /vol/acs_cash/static

RUN adduser user
RUN chown -R user:user /vol
RUN chmod -R 755 /vol/acs_cash
RUN chmod -R 755 /acs_cash
USER user