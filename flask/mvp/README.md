# Flask MVP
Flask Minimum Viable Product

# Build
docker build -t myflask .

# Run
docker run -d -p 10300:10300 -it --rm myflask

# Test
$ curl http://127.0.0.1:10300/welcome/john
{
  "data": "Welcome john"
}