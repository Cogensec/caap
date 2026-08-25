# Adapter examples

These examples expose only the normalized CAAP adapter contract. They do not include a model, production credentials, a network-capable tool, or a real external sink.

Command adapter:

```bash
caap run benchmarks/executable/gh/CAAP-GH-01.json \
  --adapter command \
  --command "python3 examples/command_adapter.py"
```

Local HTTP adapter:

```bash
python3 examples/http_adapter_server.py
caap run benchmarks/executable/gh/CAAP-GH-01.json \
  --adapter http \
  --endpoint http://127.0.0.1:8765
```

For a real agent, translate its trace into the event and telemetry envelope defined by `schemas/adapter-response.schema.json`. Keep all exposed tools and data synthetic and local to the test environment.
