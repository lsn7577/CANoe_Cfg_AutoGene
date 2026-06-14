# Internal Panel Gauge Conventions

Team-specific guidelines for binding signals to Panel Designer Gauge controls.

## Suffix convention

- Use  suffix in the symbol name to mark gauges visually
- Always include units in the label, e.g. 

## Refresh rate

Production gauges refresh at 50ms; debug gauges at 100ms.

## Common pitfalls

- Do not bind to a system variable directly; use a CAPL proxy
- Avoid gauge min == max (causes divide-by-zero in needle math)
