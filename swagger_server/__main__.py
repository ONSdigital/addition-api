#!/usr/bin/env python3

from os import getenv, getcwd
from pathlib import Path

from connexion import App
from flask_cors import CORS

from swagger_server.encoder import JSONEncoder

if __name__ == '__main__':
    cf_app_env = getenv('VCAP_APPLICATION')
    in_cf_env = cf_app_env is not None
    if in_cf_env:
        import yaml
        import json
        cwd = getcwd()
        config = './swagger_server/swagger/swagger.yaml'
        if Path(config).is_file():
            with open(config) as io:
                code = yaml.load(io)
            code['host'] = json.loads(cf_app_env)['application_uris'][0]
            with open(config, 'w') as io:
                io.write(yaml.dump(code))

    app = App(__name__, specification_dir='./swagger/')
    CORS(app.app)
    app.app.json_encoder = JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'ONS Microservice'})
    app.run(host='0.0.0.0', port=int(getenv('PORT', '5000')), debug=not in_cf_env)
