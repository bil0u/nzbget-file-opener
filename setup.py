import setuptools


def readme():
    with open('README.rst') as f:
        return f.read()


setuptools.setup(
    name='package-name',
    version='0.1',
    description='package-name description',
    long_description=readme(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Topic :: Text Processing :: Linguistic',
    ],
    keywords='package-name',
    url='http://github.com/bil0u/package-name',
    author='Ugo Popée',
    author_email='ugo.popee@me.com',
    license='MIT',
    packages=[
        'package-name'
    ],
    include_package_data=True,
    zip_safe=False
)
