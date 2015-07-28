##
# Bunch of usage information
help () {

    # help and usage message
    echo "Usage: ./run.sh <OPTION>"
    echo "Below are the various options and their descriptions after a dash"
    echo ""
    echo ""
}

# Change directory for to run.sh
OLDDIR=$(pwd)
DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
cd $DIR

##
# Deploy the production application
#
deploy () {
    git fetch
    git reset --hard origin/production

    reload
}

##
# Reloads the production application
#
reload () {
    # install python requirements
    pip3 install -r src/hackerapi/requirements.txt

    export PYTHONPATH=$(pwd)/src

    # run migrations
    python3 production/migrate.py --environment=production

    if [[ $(cat /tmp/kerbos-active) = '0' ]]; then
        TO_PORT="1"
        FROM_PORT="0"
    else
        TO_PORT="0"
        FROM_PORT="1"
    fi

    # start new application
    supervisorctl -c src/hackerapi/production/config/supervisor.conf "start flask-800${TO_PORT}:*"

    # give the new application some time to start
    sleep 5

    # shuffle out old application
    rm /etc/nginx/sites-enabled/hackerapi
    ln -s /root/kerbos-machine/production/hackerapi-800${TO_PORT} /etc/nginx/sites-enabled/kerbos

    # we need to sleep to have nginx see the new file for reloading?
    sleep 2

    nginx -s reload

    supervisorctl -c src/hackerapi/production/config/supervisor.conf "stop flask-800${FROM_PORT}:*"
    echo "$TO_PORT" > /var/tmp/hackerapi-active
}

if [[ ${1} = "supervise" ]]; then
    supervisorctl -c supervisor.conf
elif [[ ${1} = "deploy" ]]; then
    deploy
elif [[ ${1} = "reload" ]]; then
    deploy
else
    help
fi

# return to our original directory pre ./run.sh
cd $OLDDIR