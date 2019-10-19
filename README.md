## NZBget file opener

### Install

```shell script
pip install nzbget-file-opener
```

### Use

```shell script
nzbget-file-opener file_1.nzb path/file_2.nzb ...
```

### Scripts

Available `pipenv run` scripts :

- `app` : runs the application
- `build` : build the app artifacts
- `deploy-test` : deploy to [test.pypi](https://test.pypi.org)
- `deploy` : deploy to [pypi](https://pypi.org)
- `clean` : clean the artifacts created with the `build` script

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