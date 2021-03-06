import os

DEFAULT_TIMEOUT = 10
LABEL_CONTAINER_NUMBER = 'com.docker.compose.container-number'
LABEL_ONE_OFF = 'com.docker.compose.oneoff'
LABEL_PROJECT = 'com.docker.compose.project'
LABEL_SERVICE = 'com.docker.compose.service'
LABEL_VERSION = 'com.docker.compose.version'
LABEL_CONFIG_HASH = 'com.docker.compose.config-hash'
HTTP_TIMEOUT = int(os.environ.get('COMPOSE_HTTP_TIMEOUT', os.environ.get('DOCKER_CLIENT_TIMEOUT', 60)))
