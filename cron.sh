#!/bin/bash

sudo letsencrypt renew
cd /home/projects/nginx-load-balancer/docker
sudo /home/projects/nginx-load-balancer/docker/import_certificates.sh
