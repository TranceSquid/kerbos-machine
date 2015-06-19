if [ $1 = 'env' ]; then
    source ./.env/bin/activate
fi

echo "Usage:"
echo "  run.sh env => enters virtualenv"