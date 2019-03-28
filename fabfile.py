from fabric.api import run, env, cd, sudo

env.use_ssh_config = True
env.hosts = ["Beryllium", "Carbon", "Nitrogen", "Oxygen"]


def deploy_and_reload():
    "Runs 'git pull' and reloads Nginx"
    with cd('/home/projects/nginx-load-balancer/docker'):
        run('git pull git@github.com:openstate/nginx-load-balancer.git')
        sudo('./reload.sh')


def deploy_and_restart():
    "Runs 'git pull', restarts docker-compose (required if you change nginx.conf) and reloads Nginx"
    with cd('/home/projects/nginx-load-balancer/docker'):
        run('git pull git@github.com:openstate/nginx-load-balancer.git')
        sudo('docker-compose restart')
        sudo('./reload.sh')


def deploy_and_up():
    "Runs 'git pull', docker-compose up -d (required if you update Nginx/Certbot version) and reloads Nginx"
    with cd('/home/projects/nginx-load-balancer/docker'):
        run('git pull git@github.com:openstate/nginx-load-balancer.git')
        sudo('docker-compose up -d')
        sudo('./reload.sh')
