# Local development environment for IGV.js + htsget-rs

Production htsget-rs servers can be deployed to several cloud providers via [htsget-deploy], however a local
dev environment that bypasses CORS for convenience is very useful.

**WARNING:** Never use this environment in production, this is only meant for localhost-only debugging and development.

## Quickstart

Assuming you have `python3` and `docker-(compose)` installed on your local machine...

```sh
git clone --recursive https://github.com/umccr/htsget-igv.js
bin/start.sh
```

[htsget-deploy]: https://github.com/umccr/htsget-deploy
