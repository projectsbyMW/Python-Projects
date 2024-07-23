FROM ubuntu:latest

RUN apt-get update && \
    apt-get -y install fortune cowsay 

RUN apt-get install -y netcat-openbsd

RUN cp -pr /usr/games/fortune /bin/fortune
RUN cp -pr /usr/games/cowsay /bin/cowsay


#FROM debian:latest

#RUN apt-get update -y && apt-get install git cowsay fortune netcat-openbsd -y

#WORKDIR /app

#ENV PATH="$PATH:/usr/games"

COPY wisecow.sh /app/wisecow.sh

RUN chmod +x /app/wisecow.sh

EXPOSE 4499

ENTRYPOINT ["/usr/bin/env","/app/wisecow.sh"]
