FROM nginxinc/nginx-unprivileged:1-alpine

COPY ./default.conf /etc/nginx/conf.d/default.conf
COPY ./uwsgi_params /etc/nginx/uwsgi_params

USER root

# Create a directory for log files
RUN mkdir -p /var/log/nginx

# Set permissions for the log directory and log file
RUN chmod -R 777 /var/log/nginx

RUN mkdir -p /vol/acs_cash/static
RUN chmod 777 /vol/acs_cash/static
RUN adduser -D user
RUN chown -R user:user /vol/
RUN chown -R user:user /var/

USER nginx
