# SCC_StateTransitionInd

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_StateTransitionInd ( byte SessionID[], dword OldState, dword NewState )
```

## Description

The callback is called each time the internal state machine switches its state, i.e. usually when a new message is received. Use SCC_GetStateName for a string representation of the state IDs.

## Return Values

—

## Availability

| Since Version |
|---|
