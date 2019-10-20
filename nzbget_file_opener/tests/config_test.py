import os

import pytest

from nzbget_file_opener.args import get_arguments
from nzbget_file_opener.config import AppConfig


def fullpath(file):
    return f'nzbget_file_opener/tests/{file}'


def test_config_default():
    """ Ensures that the default config match the default app settings """
    # Preparation
    config = AppConfig()
    # Tests
    assert config.url == 'http://localhost:6789'


def test_config_env_basic():
    """ Ensures that loading a config from env works """
    # Preparation
    config = AppConfig()

    # Tests
    os.environ['NZBGET_URL'] = 'http://envhost'
    config.read_env()
    assert config.url == 'http://envhost:6789'

    os.environ['NZBGET_URL'] = 'http://envhost:1234'
    config.read_env()
    assert config.url == 'http://envhost:1234'

    os.environ['NZBGET_USERNAME'] = 'envuser'
    config.read_env()
    assert config.url == 'http://envhost:1234'

    os.environ['NZBGET_PASSWORD'] = 'envpass'
    config.read_env()
    assert config.url == 'http://envuser:envpass@envhost:1234'


def test_config_file_basic(tmpdir):
    """ Ensures that loading a config from a file works """
    # Preparation
    config = AppConfig()
    print(os.getcwd())
    config.read_file(fullpath('nzbgetrc'))
    assert config.url == 'http://fileuser:filepass@filehost:1234'


def test_config_args_basic(tmpdir):
    """ Ensures that loading a config from script args works """
    # Preparation
    config = AppConfig()

    # Test
    args_list = ['-n', 'argshost', fullpath('file.nzb')]
    args = get_arguments(args_list)
    config.read_args(args)
    assert config.url == 'http://argshost:6789'

    args_list = ['-n', 'argshost:1234', fullpath('file.nzb')]
    args = get_arguments(args_list)
    config.read_args(args)
    assert config.url == 'http://argshost:1234'

    with pytest.raises(SystemExit) as exc:
        args_list = ['-n', 'argshost:1234', '-u', 'argsuser', fullpath('file.nzb')]
        args = get_arguments(args_list)
    assert exc.type == SystemExit
    assert exc.value.code == 2

    args_list = ['-n', 'argshost:1234', '-u', 'argsuser', '-p', 'argspass', fullpath('file.nzb')]
    args = get_arguments(args_list)
    config.read_args(args)
    assert config.url == 'http://argsuser:argspass@argshost:1234'

    args_list = ['-l', fullpath('nzbgetrc'), '-d', 'otherhost', fullpath('file.nzb')]
    args = get_arguments(args_list)
    config.read_args(args)
    assert config.url == 'http://otheruser:otherpass@otherhost:6789'
