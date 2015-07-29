from fabric.api import env, run, cd, task

@task
def staging():
    env.use_ssh_config = True
    env.hosts = ['kerbos-staging.trancesquid.io']

@task
def prod():
    env.use_ssh_config = True
    env.hosts = ['kerbos.trancesquid.io']

def update():
    with cd('/kerbos'):
        run('git fetch')
        run('git reset --hard origin/production')

def migrate():
    with cd('/kerbos'):
        run('python3 manage.py migrate')

def reload_application():
    with cd('/kerbos'):
        run("""
            supervisorctl -c production/supervisor.conf status |
            grep RUNNING |
            grep gunicorn |
            awk -F' ' '{print $4}' |
            sed -e 's/,$//' |
            paste -sd' ' |
            xargs kill
            """)

@task
def deploy():
    update()
    migrate()
    reload_application()

@task
def reload():
    reload_application()
