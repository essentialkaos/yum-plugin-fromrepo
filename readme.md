## `yum-plugin-fromrepo` [![Maintainability](https://api.codeclimate.com/v1/badges/f34b79393e096c4d7a75/maintainability)](https://codeclimate.com/github/essentialkaos/yum-plugin-fromrepo/maintainability) [![codebeat badge](https://codebeat.co/badges/1b73d8db-e03c-4309-987c-45fe71a3e5a8)](https://codebeat.co/projects/github-com-essentialkaos-yum-plugin-fromrepo-master) [![License](https://gh.kaos.io/ekol.svg)](https://essentialkaos.com/ekol)

`yum-plugin-fromrepo` is YUM plugin to simplify working with only one repository. Plugin add option `--repo` which allows you to specify one repository for some action (`install` _for example_).

### Installation

#### From ESSENTIAL KAOS Public repo for RHEL6/CentOS6

```
[sudo] yum install -y https://yum.kaos.io/6/release/x86_64/kaos-repo-8.0-0.el6.noarch.rpm
[sudo] yum install yum-plugin-fromrepo
```

#### From ESSENTIAL KAOS Public repo for RHEL7/CentOS7

```
[sudo] yum install -y https://yum.kaos.io/7/release/x86_64/kaos-repo-8.0-0.el7.noarch.rpm
[sudo] yum install yum-plugin-fromrepo
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

### License

[EKOL](https://essentialkaos.com/ekol)

<p align="center"><a href="https://essentialkaos.com"><img src="https://gh.kaos.io/ekgh.svg"/></a></p>
