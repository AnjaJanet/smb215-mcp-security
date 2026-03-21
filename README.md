# MCP Demo (fastmcp calculator)

This folder contains a small demo of `FastMCP` Python tool server, with calculator operations exposed as MCP tools.

## Files

- `fastmcp_calculator.py`: safe calculator; tools: `multiply`, `add` (alias), `subtract`, `divide`.
- `fastmcp_calculator_prompt_injection.py`: same calculator but with a prompt-injection payload in docstring for testing policy/agent safety.
- `fastmcp_calculator_tool_abuse.py`: same calculator with a tool-abuse payload in docstring for testing guardrails.
- `pawned.txt`: artifact used in the prompt-injection samples.

## Requirements

- Python 3.11+ (3.12 is used by the local environment) 
- `fastmcp`, `mcp` and dependencies

Install dependencies:

```bash
cd demo
python -m pip install -r requirements.txt
```

## Usage

Run a demo server (STDIO transport):

```bash
cd demo
python fastmcp_calculator.py
```

Then send JSON messages through stdin/stdout according to MCP protocol, or use a client library that supports MCP.

## Examples

From shell (simple):

```bash
echo '{"query":"multiply", "args":{"a":5,"b":7}}' | python fastmcp_calculator.py
```

If using `mcp` tool wrapper in your application, import and call like normal.

## Note on security evaluation

The `*_prompt_injection.py` and `*_tool_abuse.py` variants are intentionally crafted to test agentGuard and injection defense behavior. Do not use them in production.
