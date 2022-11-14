# Stock Quotes service

This is a small educational microservice that serves as an exercise to work with FastAPI and API data providers

# Build

```bash
docker build . --tag stock-quote-service:latest
```

# Run with defaults
```bash
docker run -p 8080:80 stock-quote-service:latest
```

# Run with environment variables
```bash
DATA_PROVIDERS='YAHOO, ALPHA_VANTAGE'
ALPHA_VANTAGE_API_KEY='FEIKG8A0RFEIKG8A0R'

docker run -p 8080:80 \
    -e DATA_PROVIDERS=${DATA_PROVIDERS} \
    -e ALPHA_VANTAGE_API_KEY=${ALPHA_VANTAGE_API_KEY} \
    stock-quote-service:latest
```
