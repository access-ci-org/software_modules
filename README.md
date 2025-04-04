# software_modules
List software modules per resource or group


## Requirements
* docker


## Usage
Run from docker image
* `docker login https://ghcr.io`
  * Login with username and PersonalAccessToken
    * See also: [Managing Your Personal Access Tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
* `curl -o go_access_software_modules.sh
  https://raw.githubusercontent.com/access-ci-org/software_modules/refs/heads/production/go.sh`
* `bash go_access_software_modules.sh`
* `python -m src.report -p 1>/home/software_modules.json`


## Developer
Alternative to "docker login", download the repo and run `docker build` locally
* `git clone https://github.com/access-ci-org/software_modules.git`
* `cd software_modules`
* `make dev`
* `python -m src.report -p 1>/home/software_modules.json`
