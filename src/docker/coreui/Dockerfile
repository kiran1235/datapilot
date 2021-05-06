FROM node:14-alpine
WORKDIR /app

RUN apk add bash curl git openssh gnupg unzip sqlite --no-cache && \
    npx create-react-app coreui && \
    curl -OL https://github.com/coreui/coreui-free-react-admin-template/archive/refs/tags/3.2.1.zip && \
    unzip 3.2.1.zip && \
    ls -ltrh && \
    cp -R coreui-free-react-admin-template-3.2.1/. coreui && \
    cd coreui && \
    ls -ltrh && \
    yarn add react-redux && \
    yarn build


# production environment
FROM nginx:stable-alpine
COPY --from=0 /app/coreui/build/ /usr/share/nginx/html
RUN cd /usr/share/nginx/html && ls -ltrh
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
