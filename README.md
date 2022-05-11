<p align="center"><a href="#readme"><img src="https://gh.kaos.st/yum-plugin-fromrepo.svg"/></a></p>

<p align="center">
  <a href="https://kaos.sh/w/swptop/ci"><img src="https://kaos.sh/w/swptop/ci.svg" alt="GitHub Actions CI Status" /></a>
  <a hre="https://codeclimate.com/github/essentialkaos/yum-plugin-fromrepo/maintainability"><img src="https://api.codeclimate.com/v1/badges/f34b79393e096c4d7a75/maintainability"></a>
  <a href="https://kaos.sh/b/swptop"><img src="https://kaos.sh/b/1b73d8db-e03c-4309-987c-45fe71a3e5a8.svg" alt="codebeat badge" /></a>
  <a href="#license"><img src="https://gh.kaos.st/apache2.svg"></a>
</p>

<p align="center"><a href="#installation">Installation</a> • <a href="#usage">Usage</a> • <a href="#build-status">Build Status</a> • <a href="#contributing">Contributing</a> • <a href="#license">License</a></p>

<br/>

`yum-plugin-fromrepo` is YUM plugin to simplify working with only one repository. Plugin add option `--repo` which allows you to specify one repository for some action (`install` _for example_).

### Installation

#### From ESSENTIAL KAOS Public repository

```
sudo yum install -y https://yum.kaos.st/get/$(uname -r).rpm
sudo yum install yum-plugin-fromrepo
```

### Usage

```bash
# Install goaccess from epel repository
yum --repo=epel install goaccess

# Update webkaos to latest version available in testing repo
yum --repo=kaos-testing update webkaos

# Clean metadata and try to install latest version of redis from testing repo
yum --repo=kaos-testing clean expire-cache && yum --repo=kaos-testing install redis
```

### Build Status

| Branch | Status |
|--------|--------|
| `master` | [![CI](https://kaos.sh/w/swptop/ci.svg?branch=master)](https://kaos.sh/w/swptop/ci?query=branch:master) |
| `develop` | [![CI](https://kaos.sh/w/swptop/ci.svg?branch=master)](https://kaos.sh/w/swptop/ci?query=branch:develop) |

### Contributing

Before contributing to this project please read our [Contributing Guidelines](https://github.com/essentialkaos/contributing-guidelines#contributing-guidelines).

### License

[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)

<p align="center"><a href="https://essentialkaos.com"><img src="https://gh.kaos.st/ekgh.svg"/></a></p>
