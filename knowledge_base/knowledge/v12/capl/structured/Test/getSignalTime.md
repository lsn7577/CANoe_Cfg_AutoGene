# getSignalTime

> Category: `Test` | Type: `function`

## Syntax

```c
dword getSignalTime(Signal aSignal); // form 1
```

## Description

Gets the time point (unit: 10 microseconds) relative to the measurement start at which the signal was last sent on the bus.

It is recommended to use form 1. The runtime environment is faster with form 1, because the signal object is determined during CAPL code compilation before measurement start. With form 2 the signal object is determined during runtime which influences the performance

## Return Values

Time point or 0 if the signal was not sent yet.

## Example

```c
dword timePoint;
timePoint = getSignalTime(Node_SUT::CrashDetected);
```

## Availability

| Since Version |
|---|
