# ROUTING CONFIG — Anti-Stall Logic

## Every API Call Uses This:
```json
{
  "provider": {
    "sort": "latency",
    "allow_fallbacks": true,
    "partition": "none",
    "preferred_max_latency": {"p50": 5000, "p90": 15000},
    "preferred_min_throughput": {"p50": 30}
  },
  "max_price": {"input": 0.50, "output": 1.00}
}
```

## What This Does:
- sort: latency → picks fastest provider RIGHT NOW
- partition: none → routes across ALL models globally, not just primary
- p50 < 5s → prefers providers responding under 5 seconds
- p90 < 15s → hard deprioritises anything slower than 15 seconds
- throughput > 30 tok/s → prefers fast generators
- max_price → circuit breaker prevents expensive fallbacks (blocks Opus)

## Timeout Rule:
If ANY model takes >30 seconds to start responding → ABORT → try next model.
Never wait. A 30-second stall = 30 seconds of zero content.

## Self-Healing:
- 3 consecutive stalls → switch ALL workers to openrouter/free for 10 minutes
- 5 errors from one model in 1 hour → blacklist that model for 30 minutes
- Report blacklists to Daniel via Telegram
