FROM nginxinc/nginx-unprivileged:1-alpine

COPY ./default.conf /etc/nginx/conf.d/default.conf
COPY ./uwsgi_params /etc/nginx/uwsgi_params

USER root

RUN mkdir -p /vol/acs_cash/static
RUN chmod 777 /vol/acs_cash/static
RUN adduser -D user
RUN chown -R user:user /vol/

USER nginx
