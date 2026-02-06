import argparse

parser = argparse.ArgumentParser(
    description="Simple DevOps CLI tool"
)

parser.add_argument(
    "--server",
    required=True,
    help="Server name"
)

parser.add_argument(
    "--action",
    choices=["start", "stop", "status"],
    required=True,
    help="Action to perform"
)

args = parser.parse_args()

print(f"Server: {args.server}")
print(f"Action: {args.action}")

if args.action == "start":
    print(f"Starting {args.server}...")
elif args.action == "stop":
    print(f"Stopping {args.server}...")
else:
    print(f"Checking status of {args.server}...")
