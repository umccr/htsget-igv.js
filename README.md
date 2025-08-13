# Local development environment for IGV.js + htsget-rs

Production htsget-rs servers can be deployed to several cloud providers via [htsget-deploy], however a local
dev environment that bypasses CORS for convenience is very useful.

**WARNING:** Never use this environment in production, this is only meant for localhost-only debugging and development.

## Quickstart

Open up two consoles, first one tilting up an htsget-rs instance:

```sh
docker compose up
```

The second one serving up IGV.js's static assets:

```sh
python -
```

[htsget-deploy]: https://github.com/umccr/htsget-deploy
