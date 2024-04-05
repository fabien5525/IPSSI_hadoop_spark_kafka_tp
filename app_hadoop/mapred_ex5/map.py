import sys
import json

json_file = json.load(sys.stdin)

print(json.dumps(json_file))