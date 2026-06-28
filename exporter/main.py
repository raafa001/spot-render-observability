from prometheus_client import Counter, Gauge, Histogram, start_http_server

RENDER_SUCCESS = Counter("render_success_total", "Completed renders", ["project", "artist"])
RENDER_ERROR = Counter("render_error_total", "Failed renders", ["project", "artist"])
RENDER_QUEUE = Gauge("render_queue_total", "Files waiting per project", ["project"])
RENDER_DURATION = Histogram("render_duration_seconds", "Render duration", buckets=(60, 120, 300, 900, 1800))
CANARY_REQ = Counter("render_canary_requests_total", "Requests per rollout version", ["version", "status"])


def main():
    start_http_server(9100)
    print("Exporter listening on :9100")
    import time

    while True:
        time.sleep(60)


if __name__ == "__main__":
    main()
