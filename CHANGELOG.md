# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

| Change Type   | Description                            |
| :------------ | :------------------------------------- |
| Added         | for new features.                      |
| Changed       | for changes in existing functionality. |
| Deprecated    | for soon-to-be removed features.       |
| Removed       | for now removed features.              |
| Fixed         | for any bug fixes.                     |
| Security      | in case of vulnerabilities.            |

## [Unreleased]

## [2.0.0] - 2020-04-02

### Added

- Support for python 3.8 and ansible 2.9
- Support for Centos 8

### Changed

- Changed molecule version to 3.x

### Removed

- Removed support for ansible 2.5, 2.6, 2.7
- Removed support for python 2.7

## [1.3.0] - 2018-11-5

### Added

- Added testing of requirements.yml for other roles

### Changed

- Changed deprecated apt and yum install settings
- Travis now uses a matrix of tests for each tox scenario
- Moved .yamllint into molecule scenario
- Updated README
- Changed Vagrantfile to use most recent ansible and docker-compose
- Molecule default scenario will build platforms based on environmental variables set in tox ( MOLECULE_DISTRO & MOLECULE_DOCKER_COMMAND )
- Updated Tox to test multiple operating systems and ansible versions

### Removed

- Removed building docker container within repository
- Removed static molecule create/destroy/prepare files
- Removed old makefile

## [1.2.1] - 2018-04-20

### Changed

- Updated test suite to use molecule

### Removed

- Removed tests for Debian Jessie

## [1.2.0] - 2017-11-29

### Changed

- Self-Signed certificate extension from .cer to .crt

## [1.0.1] - 2017-11-14

### Added

- Ansible Galaxy metadata file.

[Unreleased]: https://github.com/joshuacherry/ansible-role-openssl/compare/2.0.0...HEAD
[2.0.0]: https://github.com/joshuacherry/ansible-role-openssl/compare/1.3.0...2.0.0
[1.3.0]: https://github.com/joshuacherry/ansible-role-openssl/compare/1.2.1...1.3.0
[1.2.1]: https://github.com/joshuacherry/ansible-role-openssl/compare/1.2.0...1.2.1
[1.2.0]: https://github.com/joshuacherry/ansible-role-openssl/compare/1.0.1...1.2.0
[1.0.1]: https://github.com/joshuacherry/ansible-role-openssl/compare/1.0.0...1.0.1