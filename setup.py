from setuptools import setup, find_packages

setup(
    name="qcloud_tim",
    version='1.1.11',
    packages=find_packages(exclude=('tests', 'tests.*')),
    description="A package for qcloud im(tim), Implement REST API.",
    author="Severus Well",
    author_email='thinkweiwei@msn.com',
    url="https://github.com/SeverusWell/qcloud_tim",
    keywords=['qcloud', 'Tencent', 'im', 'tim', 'SDK'],
    classifiers=[
        'Environment :: Console',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    install_requires=[
        "enum34>=1.1.4; python_version < '3.4'",
        'tls-sig-api-v2>=1.1',
        'requests>=2.4.3'
    ]
)
