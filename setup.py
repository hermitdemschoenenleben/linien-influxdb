import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="linien-influxdb",
    version='0.0.2',
    author="Benjamin Wiegand",
    author_email="highwaychile@posteo.de",
    description="Lock status of linien to influxdb",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/hermitdemschoenenleben/linien-influxdb",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    scripts=[
        'bin/linien-influxdb'
    ],
    install_requires=[
        'linien', 'rpyc', 'plumbum', 'click'
    ]
)