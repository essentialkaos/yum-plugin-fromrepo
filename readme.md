## `yum-plugin-fromrepo` [![License](https://gh.kaos.io/ekol.svg)](https://essentialkaos.com/ekol)

`yum-plugin-fromrepo` is YUM plugin to simplify working with only one repository. Plugin add option `--from` which allows you to specify one repository for some action (`install` _for example_).

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

```
[sudo] yum --from=epel install goaccess

[sudo] yum --from=kaos-testing update webkaos
```

### License

[EKOL](https://essentialkaos.com/ekol)

<p align="center"><a href="https://essentialkaos.com"><img src="https://gh.kaos.io/ekgh.svg"/></a></p>
