# Market Analysis API

Uma API para analisar os mercados do Brasil e do mundo

# Build

```bash
docker build . --tag market-analysis-api:latest
```

# Run with defaults
```bash
docker run -p 8080:80 market-analysis-api:latest
```

# Run with environment variables
```bash
DATA_PROVIDERS='YAHOO, ALPHA_VANTAGE'
ALPHA_VANTAGE_API_KEY='FEIKG8A0RFEIKG8A0R'

docker run -p 8080:80 \
    -e DATA_PROVIDERS=${DATA_PROVIDERS} \
    -e ALPHA_VANTAGE_API_KEY=${ALPHA_VANTAGE_API_KEY} \
    market-analysis-api:latest
```
