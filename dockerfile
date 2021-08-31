FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get -y install unzip wget python3-pip

# install google chrome
RUN wget -c https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb; exit 0
RUN apt-get install -f -y
RUN ln -fs /usr/share/zoneinfo/Asia/Taipei /etc/localtime
RUN dpkg-reconfigure -f noninteractive tzdata

# install chromedriver
RUN wget -N https://chromedriver.storage.googleapis.com/92.0.4515.107/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip && chmod +x chromedriver
RUN mv -f chromedriver /usr/local/share/chromedriver
RUN ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
RUN ln -s /usr/local/share/chromedriver /usr/bin/chromedriver

# install selenium
RUN pip3 install selenium

COPY auto-clock-in.py .

ENTRYPOINT [ "python3", "/auto-clock-in.py" ]