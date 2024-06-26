from setuptools import setup

setup(
    name='email',
    version='0.1',
    py_modules=['main'],
    install_requires=[
        'click'
    ],
    entry_points={
        'console_scripts': [
            'sendto=main:aboutme',
            'mails=mails:mails',
            'sends:=sends:sends'
        ],
    },
)
