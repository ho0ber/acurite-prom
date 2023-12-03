from prometheus_client import start_http_server
from prometheus_client import Gauge
import json

LABELS = ["model", "id", "name", "channel", "mic"]
NAMES = {
    8184: "henhouse-west",
    11289: "new",
}

t = Gauge("temperature", "Humidity", LABELS)
h = Gauge("humidity", "Humidity", LABELS)
b = Gauge("battery_ok", "Battery status", LABELS)

start_http_server(8080)

while True:
    input_string = input()
    reading = json.loads(input_string)
    labels = [
        reading.get("model"),
        reading.get("id"),
        NAMES.get(reading.get("id"), reading.get("id")),
        reading.get("channel"),
        reading.get("mic"),
    ]
    t.labels(*labels).set(reading.get("temperature_F"))
    h.labels(*labels).set(reading.get("humidity"))
    b.labels(*labels).set(reading.get("battery_ok"))
