#!/bin/bash
# This script adds all files required for HTTPS to the nginx-load-balancer
# container

# Add your domain to the domains array
domains=(
)

directory="/etc/letsencrypt/live/"

sudo docker exec docker_c-nginx-load-balancer_1 mkdir -p /etc/ssl/private/
sudo docker cp dhparams.pem docker_c-nginx-load-balancer_1:/etc/ssl/private/

for domain in "${domains[@]}"
do
    echo *** Importing certificate for "$domain"

    # Create the directory if it does not exist
    sudo docker exec docker_c-nginx-load-balancer_1 mkdir -p "$directory""$domain"

    # Dereference symlinks to fullchain and privkey
    fullchain=`sudo readlink -f /etc/letsencrypt/live/$domain/fullchain.pem`
    privkey=`sudo readlink -f /etc/letsencrypt/live/$domain/privkey.pem`

    # Copy fullchain and privkey to the docker_c-nginx-load-balancer_1 docker container
    sudo docker cp $fullchain docker_c-nginx-load-balancer_1:/etc/letsencrypt/live/$domain/fullchain.pem
    sudo docker cp $privkey docker_c-nginx-load-balancer_1:/etc/letsencrypt/live/$domain/privkey.pem
done

# Reload Nginx
echo *** Reload configuration
sudo docker exec docker_c-nginx-load-balancer_1 nginx -t
if [ $? -eq 0 ]; then
  sudo docker exec docker_c-nginx-load-balancer_1 nginx -s reload
else
  printf "\nDID NOT RELOAD NGINX CONFIG: NGINX CONFIG GAVE AN ERROR!\n"
fi

