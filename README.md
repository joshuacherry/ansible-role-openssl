# ansible-role-openssl

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://travis-ci.org/joshuacherry/ansible-role-openssl.svg?branch=master)](https://travis-ci.org/joshuacherry/ansible-role-openssl)
![Ansible](https://img.shields.io/badge/ansible-2.4.1.0-green.svg)

Manage SSL certificates on a linux server.

## Requirements

- Ansible >= 2.4.1.0

## Install

### Install from GitHub

`ansible-galaxy install git+https://github.com/joshuacherry/ansible-role-openssl.git`

## Features

- Create Self Signed Certificate
- Manage multiple predefined certificates

| OS            | Openssl Certificates  |
| :------------ | :-----------:         |
| Debian 8      | ✓                     |
| Ubuntu 16.04  | ✓                     |
| Centos 7      | ✓                     |

## Versioning

[Semantic Versioning](http://semver.org/)

For the versions available, see the [tags on this repository](https://github.com/joshuacherry/ansible-role-openssl/tags).

Additionaly you can see what change in each version in the [CHANGELOG.md](CHANGELOG.md) file.

## Role variables

Look to the [defaults](defaults/main.yml) properties file to see the possible configuration properties.

## Testing

This role includes a Vagrantfile used with a Docker-based test harness that approximates the Travis CI setup for integration testing. Using Vagrant allows all contributors to test on the same platform and avoid false test failures due to untested or incompatible docker versions.

1. Install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/).
1. Run `vagrant up` from the same directory as the Vagrantfile in this repository.
1. SSH into the VM with: `vagrant ssh`
1. Run tests with `make`.

### Testing with Docker and inspec

```bash
make -C /vagrant xenial64 test
```

See `make help` for more information including a full list of available targets.

## Example Playbook

### Basic Setup with all defaults

```yaml
---
- name: Playbook for ansible-role-openssl
  hosts: all

  tasks:
  - include_role:
      name: ansible-role-openssl
```

### Setup with custom certificates

```yaml
---
- name: Playbook for ansible-role-openssl
  hosts: all

  tasks:
  - include_role:
      name: ansible-role-openssl
  vars:
    openssl_certs_path: /etc/pki/tls/certs
    openssl_keys_path: /etc/pki/tls/private
    openssl_self_signed:
      - { name: 'role_test_cert',
          country: 'US',
          state: 'State',
          city: 'City',
          organization: 'Org Name',
          unit: 'Department Name',
          email: 'admin@fqdn',
          days: '3650'
      }
    openssl_keys: 
      - name: mycert.key
        key: |
          -----BEGIN PRIVATE KEY-----
          MULTI_LINE_CERT_KEY_GOES_HERE
          -----END PRIVATE KEY-----
      - name: myotherkey.key
        key: "myotherkeycontents"
        mode: "0664"
        owner: "root"
        group: "root"
    openssl_certs:
      - name: mycert.cer
        cert: |
          -----BEGIN CERTIFICATE-----
          FAKE_CERT_CONTENT_GOES_HERE
          SUPPORTS_MULTI_LINE
          -----END CERTIFICATE-----
      - name: myothercert.cer
        cert: "myothercertcontents"
        mode: "0664"
        owner: "root"
        group: "root"
```