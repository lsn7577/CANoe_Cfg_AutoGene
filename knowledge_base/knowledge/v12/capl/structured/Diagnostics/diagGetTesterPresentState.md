# diagGetTesterPresentState

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
diagGetTesterPresentState(char ecuQualifier[])
```

## Description

Returns the state of autonomous/cyclical Tester Present requests from CANoe to the specified or current ECU.

This function only returns the correct state if in the calling CAPL node no CAPL Callback interface for diagnostics is used.

Status:

0: sending Tester Present disabled for target ECU1: sending Tester Present enabled for target ECU

## Return Values

Error code or status

## Availability

| Since Version |
|---|
