set -o pipefail
ONS_ENV=test py.test --cov=swagger_server --cov-report xml
