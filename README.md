# devenv-batect-base-bundle

A bundle for [Batect](https://batect.dev) that provides a development container for JVM-based languages that use Gradle, with sensible default configuration.

## Usage

### Setup

Add the following to your `batect.yml`:

```yaml
include:
  - type: git
    repo: https://github.com/hbfs-cloud/devenv-batect-base-bundle.git
    ref: latest
```

## Development

Run `./batect --list-tasks` to see a list of available tasks for this project.
