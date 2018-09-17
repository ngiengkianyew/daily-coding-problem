# Process of a URL being fetched

1. Check browsers host resolution cache.
2. If IP not found, request DNS for the IP of the host/load balancing host.
3. Send a GET request to the host
4. Host responds with a payload (usually in HTML)
5. Browser renders HTML

