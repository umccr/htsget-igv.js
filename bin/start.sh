#!/bin/sh

docker compose up &
python3 -m http.server 8787 -d igv.js &
open http://localhost:8787/dev/htsget/htsget.html
