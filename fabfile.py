from fabric import Connection, Config, task
import getpass

# Hosts to run the commands on
HOSTS = ["Beryllium", "Carbon", "Oxygen", "Fluorine"]

# Name of the git repository
GIT_REPO = 'nginx-load-balancer'

# Path of the directory
DIR = '/home/projects/%s/docker' % (GIT_REPO)

sudo_pass = getpass.getpass("Enter your sudo password: ")


@task()
def deploy_and_reload(c):
    "Runs 'git pull' and reloads Nginx"
    for host in HOSTS:
        print('\n\n*** CONNECTING TO: %s' % (host))
        config = Config(overrides={'sudo': {'password': sudo_pass}})
        c = Connection(host, config=config)

        c.run(
            'cd %s && git pull git@github.com:openstate/%s.git' % (
                DIR,
                GIT_REPO
            )
        )
        c.sudo('bash -c "cd %s && ./reload.sh"' % (DIR))


@task()
def deploy_and_restart(c):
    (
        "Runs 'git pull', restarts docker-compose (required if you change "
        "nginx.conf) and reloads Nginx"
    )
    for host in HOSTS:
        print('\n\n*** CONNECTING TO: %s' % (host))
        config = Config(overrides={'sudo': {'password': sudo_pass}})
        c = Connection(host, config=config)

        c.run(
            'cd %s && git pull git@github.com:openstate/%s.git' % (
                DIR,
                GIT_REPO
            )
        )
        c.sudo('bash -c "cd %s && docker-compose restart"' % (DIR))
        c.sudo('bash -c "cd %s && ./reload.sh"' % (DIR))

@task
def deploy_and_up(c):
    (
        "Runs 'git pull', 'docker-compose up -d' (required if you update "
        "Nginx version) and reloads Nginx"
    )
    for host in HOSTS:
        print('\n\n*** CONNECTING TO: %s' % (host))
        config = Config(overrides={'sudo': {'password': sudo_pass}})
        c = Connection(host, config=config)

        c.run(
            'cd %s && git pull git@github.com:openstate/%s.git' % (
                DIR,
                GIT_REPO
            )
        )
        c.sudo('bash -c "cd %s && docker-compose up -d"' % (DIR))
        c.sudo('bash -c "cd %s && ./reload.sh"' % (DIR))


@task
def deploy_certbot(c):
    (
        "Runs 'git pull', 'docker-compose build c-certbot', 'docker-compose "
        "up -d' (required if you update Certbot version) and reloads Nginx"
    )
    for host in HOSTS:
        print('\n\n*** CONNECTING TO: %s' % (host))
        config = Config(overrides={'sudo': {'password': sudo_pass}})
        c = Connection(host, config=config)

        c.run(
            'cd %s && git pull git@github.com:openstate/%s.git' % (
                DIR,
                GIT_REPO
            )
        )
        c.sudo('bash -c "cd %s && docker-compose build c-certbot"' % (DIR))
        c.sudo('bash -c "cd %s && docker-compose up -d"' % (DIR))
        c.sudo('bash -c "cd %s && ./reload.sh"' % (DIR))
