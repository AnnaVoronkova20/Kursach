FROM nginx

# RUN rm -rf /etc/nginx/conf.d/default.conf
# RUN rm -rf /usr/share/nginx/nginx.conf
# RUN rm -rf /usr/share/nginx/html/*

# COPY nginx.conf /etc/nginx/nginx.conf
# COPY nginx.conf /etc/nginx/conf.d/default.conf

COPY ./nginx.conf /etc/default.conf

CMD ["nginx", "-c", "/etc/default.conf", "-g", "daemon off;"]