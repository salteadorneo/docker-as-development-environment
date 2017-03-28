FROM debian:latest
MAINTAINER Lucas Menendez "epucas@gmail.com"

RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install mysql-client mysql-server
RUN sed -i -e"s/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/" /etc/mysql/my.cnf

#COPY config.sql ./
#RUN service mysql start
#RUN mysql < config.sql
#RUN service mysql stop

ENTRYPOINT /usr/bin/mysqld_safe
VOLUME  ["/etc/mysql", "/var/lib/mysql"]
