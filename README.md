# runremotely
Simple CLI utility for running remote commands with synchronized directory content


## Install
Requires python 3.6 or higher.

```bash
pip install runremotely
```

This will install the `remote` command line program.

## Development setup
1. Clone this repo
1. (recommended) create a development virtual environment using conda, pipfile, virtualenv, or similar.
2. Install dependencies: `pip install -r requirements.txt`
3. Install dev version: `pip install -e .`

## Usage

#### Get help

`remote -h` or `remote [subcommand] -h`

#### Set up a remote server
```bash
remote add [arbitrary server name] [URL for ssh] [path on remote server]
```

#### Show remote servers
```bash
remote show
```

### Sync contents then run remote command on remote server
```bash
remote run [server name] [command]
```

### Sync contents then open ssh session on remote server
```bash
remote ssh [server name]
```
