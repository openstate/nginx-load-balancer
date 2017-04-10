#!/bin/bash

# Retrieve the container names for which an upstream is defined in conf/nginx.conf
containers=($(sed -nr 's/[^#.*]upstream\s+(.*) \{/\1/p' nginx/nginx.conf))

# For each container retrieve its current IP address and use it to
# replace its old IP address in its upstream section in conf/nginx.conf
for container in "${containers[@]}"
do
    echo "*** Retrieving IP address for $container"
    ip=`sudo docker inspect --format='{{range $index, $element := .NetworkSettings.Networks}}{{if eq $index "docker_nginx-load-balancer"}}{{.IPAddress}}{{end}}{{end}}' $container`
    if [[ $ip ]]
    then
        echo $ip
        sudo perl -0777 -i -pe "s/(upstream $container \{\n\s+server) \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\1 $ip/" nginx/nginx.conf
    fi
    echo
done
