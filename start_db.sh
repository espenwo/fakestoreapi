
cd docker/

if [[ -z $1 ]]
then 
    docker-compose up -d
else
    echo "unknow argument given"
fi