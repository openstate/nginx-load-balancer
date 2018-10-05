# To start the Nginx load balancer container first run the following to
# comment out the lines referencing SSL certificates as they do not
# exist yet and will crash Nginx
sed -r -i 's/(^.*.pem;$)/#\1/' nginx/conf.d/default.conf
# Start the container
sudo docker-compose up -d
# Import the certificates
sudo ./import_certificates.sh
# Uncomment the lines referencing certificates
sed -r -i 's/^#(.*.pem;$)/\1/' nginx/conf.d/default.conf
# Reload the configuration
sudo ./reload.sh
