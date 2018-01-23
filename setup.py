from distutils.core import setup
import versioneer

with open('requirements.txt', 'r') as reqfile:
    requirements = [x.strip() for x in reqfile if x.strip()]

setup(
        name='run-remotely',
        version=versioneer.get_version(),
        cmdclass=versioneer.get_cmdclass(),
        packages=['run_remotely'],
        license='Apache 2.0',
        author='Aaron Virshup',
        author_email='avirshup@gmail.com',
        description='Porcelain CLI for syncing data and running commands remotely',
        url="https://github.com/avirshup/run-remotely",
        entry_points={
                  'console_scripts': [
                      'remote = run_remotely.__main__:main'
                  ]
        },
        install_requires=requirements,

)
