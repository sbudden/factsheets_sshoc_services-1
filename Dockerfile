FROM jekyll/jekyll:4.2.0
ENV JEKYLL_ENV=production

WORKDIR /srv/jekyll
COPY . /srv/jekyll/
RUN ls

RUN npm install \
        && ls \
        && cp ./node_modules/lightbox2/dist/js/lightbox.min.js ./assets/js/lightbox.min.js \
        && cp ./node_modules/jquery/dist/jquery.min.js ./assets/js/jquery.min.js \
        && cp ./node_modules/lightbox2/dist/css/lightbox.min.css ./assets/css/lightbox.min.css \
        && bundle install

ENTRYPOINT jekyll server