from urllib.parse import urlparse

def parse_line(line):
    parts = line.strip().split(",")
    return (parts[0], parts[1], parts[2])

def is_yesterday(date_str, yesterday):
    return date_str.split('T', 1)[0] == yesterday

def to_domain(url):
    host = urlparse(url).netloc.lower()
    if host.startswith("www."):
        host = host[4:]
    return host