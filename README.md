## NZBget file opener

### Install

```shell script
pip install nzbget-file-opener
```

### Usage

```shell script
nzbget-file-opener [-h]
                   [-n HOSTNAME] [-u USERNAME] [-p PASSWORD]
                   [-l CONFIG] [-d DOMAIN]
                   [-c CATEGORY] [-P PRIORITY]
                   [--add-top] [--add-paused]
                   [-D]
                   [--app-path NZBGET_PATH]
                   files [files ...]


positional arguments:

  files                 the files to send


optional arguments:

  -h, --help            show this help message and exit

  -n HOSTNAME, --hostname HOSTNAME
                        the nzbget hostname to reach
  -u USERNAME, --username USERNAME
                        your nzbget username
  -p PASSWORD, --password PASSWORD
                        your nzbget password

  -l CONFIG, --load-config CONFIG
                        your nzbget config
  -d DOMAIN, --domain DOMAIN
                        the domain target defined in your nzbget config

  -c CATEGORY, --category CATEGORY
                        the category to use for the nzb files download
  -P PRIORITY, --priority PRIORITY
                        the category to use for the nzb files download

  --add-top             add the files to the top of queue
  --add-paused          add the files in pause state

  --app-path NZBGET_PATH
                        specify the nzbget app path to launch it if not
                        already running

  -D, --delete-files    to delete the files sent to NZBget
```

The nzbget credentials file should respect this format :
```toml
NZBGET_URL='[http|https]://hostname:port'
NZBGET_USERNAME='username'
NZBGET_PASSWORD='password'
```

###### Notes
###### - url scheme and port are optional
###### - you can also set these variables in your environment

### Scripts

Available `pipenv run` scripts :

- `install` - installs the package
- `app` - runs the application
- `test` - tests the application with [pytest](https://docs.pytest.org/en/latest/)
- `build` - build the app artifacts
- `clean` - clean the artifacts created with the `build` script
- `deploy-test` - deploy to [test.pypi](https://test.pypi.org)
- `deploy` - deploy to [pypi](https://pypi.org)

### Requirements

In order to properly run the deploy scripts, you should :

- have **[twine](https://pypi.org/project/twine/)** installed.
- have a `~/.pypirc` file filled according to the template below
    

#### `.pypirc` template    
```toml
[distutils]
index-servers=
    pypi
    testpypi

[pypi]
username: your_username
password: your_password

[testpypi]
repository: https://test.pypi.org/legacy/
username: your_username
password: your_password
```

Note: `pypi.org` and `test.pypi.org` uses two distinct databases for user accounts. You need to create an account for both domains