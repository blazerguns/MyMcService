FROM ubuntu/apache2


RUN apt-get update && apt-get install -y software-properties-common
RUN add-apt-repository ppa:ondrej/php && apt-get update
RUN apt-get install -y php5.6 php5.6-mcrypt php5.6-mbstring php5.6-curl php5.6-cli php5.6-mysql php5.6-gd php5.6-intl php5.6-xsl php5.6-zip curl
RUN curl -s https://getcomposer.org/installer | php && mv composer.phar /usr/local/bin/composer
RUN a2enmod rewrite && rm "/var/www/html/index.html"
COPY application /var/www/html/application
COPY 000-default.conf /etc/apache2/sites-available/
RUN cd /var/www/html/application && composer install 
EXPOSE 80


