# J1939TestChkCreate_AbsCycleTimeViolation

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long J1939TestChkCreate_AbsCycleTimeViolation( dword sourceAddr, dword destAddr, dword pgn, dword aMinCycleTime, dword aMaxCycleTime
```

## Description

Checks the occurrences of cyclic messages.

An event is generated if the time between the transmission of the messages is smaller than minCycleTime or larger than maxCycleTime. Not to be checked limits are set to 0; there must be at least one limit specified.

## Availability

| Up to Version |
|---|
