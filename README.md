# Local development environment for IGV.js + htsget-rs

Production htsget-rs servers can be deployed to several cloud providers via [htsget-deploy], however a local
dev environment that bypasses CORS for convenience is very useful.

**WARNING:** Never use this environment in production, this is only meant for localhost-only debugging and development.

## Quickstart

Assuming you have `docker-(compose)` installed on your local machine, run this one time one liner:

```sh
git clone --recursive https://github.com/umccr/htsget-igv.js && cd igv.js && npm install && cd ..
```

Tilt up the docker containers:

```sh
docker compose up
```

Open the browser:

```sh
open http://localhost:8787/dev/htsget/htsget.html
```

[htsget-deploy]: https://github.com/umccr/htsget-deploy
