#!/bin/bash

# Reload conf/nginx.conf
echo "*** Reload configuration"
sudo docker exec docker_c-nginx-load-balancer_1 nginx -t
if [ $? -eq 0 ]; then
  sudo docker exec docker_c-nginx-load-balancer_1 nginx -s reload
else
  printf "\nDID NOT RELOAD NGINX CONFIG: NGINX CONFIG GAVE AN ERROR!\n"
fi
