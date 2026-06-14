# C2xGetCycleTime

> Category: `Car2x` | Type: `function`

## Syntax

```c
Int64 C2xGetCycleTime(char* dbMessage);
```

## Description

Gets the cycle time for a message in milliseconds.

## Return Values

Cycle time in milliseconds or -1 for error.

## Example

```c
Int64 cycleTime;

cycleTime = C2xGetCycleTime("CAM");
```

## Availability

| Since Version |
|---|
