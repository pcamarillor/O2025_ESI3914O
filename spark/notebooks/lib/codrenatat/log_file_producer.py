import json, random, time, uuid
from pathlib import Path
from datetime import datetime, timezone
import argparse

PATHS   = ["/", "/login", "/orders", "/cart", "/api/v1/items", "/api/v1/pay"]
METHODS = ["GET", "POST", "PUT", "DELETE"]
AGENTS  = ["Chrome", "Firefox", "Safari", "Edge"]
IPS     = [f"10.0.0.{i}" for i in range(1, 51)]

STATUS_CHOICES = [200]*80 + [404]*10 + [400]*5 + [500]*5

def make_event():
    return {
        "event_time": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        "request_id": str(uuid.uuid4()),
        "ip": random.choice(IPS),
        "method": random.choice(METHODS),
        "path": random.choice(PATHS),
        "status": random.choice(STATUS_CHOICES),
        "bytes": random.randint(200, 50_000),
        "latency_ms": random.randint(3, 1500),
        "user_agent": random.choice(AGENTS),
    }

def write_file(out_dir: Path, rows: int) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    fname = out_dir / f"logs_{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')}_{random.randint(1000,9999)}.json"
    with fname.open("w", encoding="utf-8") as f:
        for _ in range(rows):
            f.write(json.dumps(make_event()) + "\n")
    return fname

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", default="spark/notebooks/labs/lab07/input_dir")
    ap.add_argument("--rows", type=int, default=80)
    ap.add_argument("--files", type=int, default=5)
    ap.add_argument("--interval", type=float, default=3.0)
    args = ap.parse_args()

    out = Path(args.output).resolve()
    print(f"[producer] writing {args.files} files to: {out}")
    for i in range(args.files):
        p = write_file(out, args.rows)
        print(f"[producer] wrote {i+1}/{args.files}: {p.name}")
        if i < args.files - 1:
            time.sleep(args.interval)

if __name__ == "__main__":
    main()

