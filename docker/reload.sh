#!/bin/bash

# Reload conf/nginx.conf
echo "*** Reload configuration"
sudo docker exec docker-c-nginx-load-balancer-1 nginx -t
if [ $? -eq 0 ]; then
  sudo docker exec docker-c-nginx-load-balancer-1 nginx -s reload
else
  printf "\nDID NOT RELOAD NGINX CONFIG: NGINX CONFIG GAVE AN ERROR!\n"
fi
