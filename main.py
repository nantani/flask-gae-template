# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# coding: utf-8
import os

from google.auth import app_engine

import mlapi


def _get_env():  # type: () -> str
    try:
        project_id = app_engine.get_project_id()
    except EnvironmentError:
        return os.getenv('MLAPI_ENV', 'development')

    env = {
        'ubie-staging': 'staging',
        'ubie-production': 'production',
    }
    return env[project_id]


app = mlapi.create_app(_get_env())


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)

