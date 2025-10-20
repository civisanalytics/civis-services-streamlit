# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Added example config.toml with Civis styling in demo_app. (#6)

### Changed

- Updated demo app's dependencies to the latest versions: (#7)
    * pandas 2.3.0 -> 2.3.3
    * scikit-learn 1.7.0 -> 1.7.2
    * streamlit 1.46.1 -> 1.50.0

### Deprecated
### Removed
### Fixed
### Security

## [1.4.0] - 2024-07-09

### Added
- Added support for an entry point script whose filename isn't `app.py`,
  in which case the user would need to specify the file path in the platform service object. (#5)

### Changed
- Updated Python version in Docker image: 3.12.5 -> 3.13.5. (#5)
- Updated demo app's dependencies to the latest versions: (#5)
    * civis 2.3.0 -> 2.7.1
    * pandas 2.2.2 -> 2.3.0
    * scikit-learn 1.5.1 -> 1.7.0
    * streamlit 1.37.1 -> 1.46.1

## [1.3.0] - 2024-08-23

### Changed
- Updated Python version in Docker image: 3.12.4 -> 3.12.5. (#4)
- Updated demo app's dependencies to the latest versions: (#4)
    * scikit-learn 1.5.0 -> 1.5.1
    * streamlit 1.35.0 -> 1.37.1
- Switched from pip to uv for faster Python dependency installation. (#4)

## [1.2.0] - 2024-06-24

### Changed
- Updated Python version in Docker image: 3.12.3 -> 3.12.4. (#3)
- Updated demo app's dependencies to the latest versions: (#3)
    * civis 2.1.0 -> 2.3.0

## [1.1.0] - 2024-05-24

### Added
- Docker image now pre-installs Python requirements for the demo app. (#2)

### Changed
- Updated demo app's dependencies to the latest versions: (#2)
    * civis 2.0.0 -> 2.1.0
    * streamlit 1.34.0 -> 1.35.0

## [1.0.0] - 2024-05-23

First release!
