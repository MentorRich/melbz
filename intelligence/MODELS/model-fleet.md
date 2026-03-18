# MODEL FLEET — Bill's Available Models
## 15+ Models for Zero-Stall Operations

---

## BRAIN (Director/Orchestrator)
| Model | Cost | Context | Role |
|-------|------|---------|------|
| MiniMax M2.1 (PRIMARY) | $0.27/$0.95 | 197K | Always-on brain. 15 providers = never stalls. |
| MiniMax M2.5 (FALLBACK 1) | $0.25/$1.20 | 197K | Same provider diversity. |
| Gemini 2.0 Flash Lite (FALLBACK 2) | $0.075/$0.30 | 1M | Google infrastructure backup. |

## CONTENT WRITERS (6 Teams, Free Models)
| Model | Cost | Context | Assigned Team |
|-------|------|---------|---------------|
| Hunter Alpha | $0.00 | 1M | Team Editorial (provocative, rankings) |
| Healer Alpha | $0.00 | 262K | Team Food (fast writer, 93 tok/s) |
| Trinity Large Preview | $0.00 | 128K | Team Nightlife (best creative prose) |
| Qwen3 Next 80B | $0.00 | 262K | Team Lifestyle (fresh ideas) |
| Step 3.5 Flash | $0.00 | 256K | Team Property (speed-efficient reasoning) |
| Nemotron 3 Super 120B | $0.00 | 262K | Team Culture (long-context coherence) |

## ADDITIONAL FREE MODELS (Backup Workers)
| Model | Cost | Context | Use For |
|-------|------|---------|---------|
| Kimi K2 | $0.00 | 131K | Quality backup writer (89 quality score) |
| Hermes 3 405B | $0.00 | 131K | Persona consistency, long articles |
| Sonoma Sky Alpha | $0.00 | 2M | Massive context processing |
| Sonoma Dusk Alpha | $0.00 | 2M | Fast parallel tool calling |
| Sherlock Think Alpha | $0.00 | 1.8M | Deep reasoning when needed |
| Aurora Alpha | $0.00 | varies | Speed-optimised reasoning |
| GLM 4.5 Air | $0.00 | varies | Agent-centric content |
| Qwen3 Coder 480B | $0.00 | 262K | Structured/technical content |
| Auto Free Router | $0.00 | 200K | Emergency — picks anything available |

## RESEARCH
| Model | Cost | Context | Role |
|-------|------|---------|------|
| Gemini Flash (Google grounding) | Free tier | 1M | Venue research, trend scanning, fact checking |

## IMAGES
| Model | Cost | Role |
|-------|------|------|
| Nano Banana (Gemini 2.5 Flash) | $0.15/$0.60 | Image generation |

---

## ROUTING LOGIC

Every API call uses:
```json
{
  "provider": {
    "sort": "latency",
    "allow_fallbacks": true,
    "partition": "none"
  }
}
```

If primary stalls >30 seconds → auto-switch to next model. Never wait. Never stall.

## TOTAL CAPACITY
- 15+ free models × 1,000 requests/day each = 15,000+ free calls/day
- Brain on paid model: ~$0.25/day
- Daily budget ceiling: $2.00
- Typical daily spend: $0.25-0.50
