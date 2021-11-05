#!/usr/bin/env bash

# Find and change to repo root directory
OS=$(uname)
if [[ "$OS" == "Darwin" ]]; then
	# OSX uses BSD readlink
	BASEDIR="$(dirname "$0")"
else
	BASEDIR=$(readlink -e "$(dirname "$0")")
fi
cd "${BASEDIR}/../.." || exit 1

CONFIG_LOCATION="test_configuration/config.json"

AUTH='--auth NoAuth()'
# NB: A prerequisite to run this command locally is to have a running instance of the rid_qualifier/mock (/monitoring/rid_qualifier/mock/run_locally.sh)

echo '{
  "locale": "che",
  "injection_targets": [
    {
      "name": "uss1",
      "injection_base_url": "http://host.docker.internal:8070/operator_auth_test"
    }
  ]
}' > ${CONFIG_LOCATION}

CONFIG='--config config.json'

OPERATOR_AUTHORIZATION_QUALIFIER="$AUTH $CONFIG"

# report.json must already exist to share correctly with the Docker container
touch $(pwd)/test_result/report.json

docker build \
    -f Dockerfile \
    -t swiss-foca/operator-data-test 

docker run --name operator-data-test \
  --rm \
  --tty \
  -e OPERATOR_AUTHORIZATION_QUALIFIER="${OPERATOR_AUTHORIZATION_QUALIFIER}" \
  -e PYTHONBUFFERED=1 \
  -v $(pwd)/test_result/report.json:/app/test_result/report.json \
  -v $(pwd)/${CONFIG_LOCATION}:/app/${CONFIG_LOCATION} \
  swiss-foca/operator-data-test \
  python operator_auth_qualifier_entry.py $OPERATOR_AUTHORIZATION_QUALIFIER

rm ${CONFIG_LOCATION}
