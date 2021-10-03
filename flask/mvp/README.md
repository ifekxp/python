# Flask MVP
Flask Minimum Viable Product

# Build
<pre><code>docker build -t myflask .</code></pre>

# Run
<pre><code>docker run -d -p 10300:10300 -it --rm myflask</code></pre>

# Test
<pre><code>
$ curl http://127.0.0.1:10300/welcome/john
{
  "data": "Welcome john"
}
</code></pre>