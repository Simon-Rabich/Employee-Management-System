from prometheus_client import Counter, Gauge, Histogram

# Prometheus metrics
USAGE_API_CALLS = Counter('api_calls', 'Number of API Calls Users Done')
SITE_VISITS = Counter('site_visits', 'Number of visits to the Blackjack site')
CPU_USAGE = Gauge('cpu_usage_percent', 'Current CPU usage in percent')
MEMORY_USAGE = Gauge('memory_usage_bytes', 'Current memory usage in bytes')
NETWORK_IO_COUNTERS = Gauge('network_io_bytes', 'Network I/O counters', ['direction'])
HTTP_REQUESTS = Counter('http_requests_total', 'Total number of HTTP requests', ['method', 'endpoint', 'status_code'])
HTTP_REQUEST_DURATION = Histogram('http_request_duration_seconds', 'Histogram of HTTP request durations', ['method', 'endpoint'])
