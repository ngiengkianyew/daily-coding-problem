# Wikipedia Crawler

## System
- Use the main page to generate a queue of links that is to be processed by the server.
- Each link is put into a queue that is processed on the server.
- The processing involves just monitoring and sending each link to a client.
- The client downloads and parses the page, stores them in the DB and adds new URLs to the queue if the last update date is greater that the date the item was stored in a distributed cache.

## Questions
- How will you reach as many pages as possible? 
  - Parse all URLs on each page and add them back to the queue.
- How can you keep track of pages that have already been visited?
  - Distributed cache
- How will you deal with your client machines being blacklisted?
  - Maybe EC2 instance provisioning once `x` amount of requests get an error code response.
- How can you update your database when Wikipedia pages are added or updated?
  - Handled by the current mechanism of distributed cache checking.
