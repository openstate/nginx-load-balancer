from fabric.api import run, env, cd, sudo

env.use_ssh_config = True
env.hosts = ["Beryllium", "Carbon", "Nitrogen", "Oxygen"]


def deploy_and_reload():
    with cd('/home/projects/nginx-load-balancer/docker'):
        run('git pull git@github.com:openstate/nginx-load-balancer.git')
        sudo('./reload.sh')


def deploy_and_up():
    with cd('/home/projects/nginx-load-balancer/docker'):
        run('git pull git@github.com:openstate/nginx-load-balancer.git')
        sudo('docker-compose up -d')
        sudo('./reload.sh')
