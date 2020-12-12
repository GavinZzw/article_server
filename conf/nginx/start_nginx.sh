#!/bin/bash
pkill -9 nginx
/usr/local/nginx/sbin/nginx -c /usr/local/nginx/conf/nginx.conf -g 'daemon off;'
