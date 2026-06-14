# getSignalTimeByTxNode

> Category: `Obsolete` | Type: `function`

## Syntax

```c
dword getSignalTimeByTxNode (dbSignal aSignal, dbNode aTxNode);
```

## Description

Gets the time point relative to the measurement start at which the signal was last sent on the bus.

## Return Values

Time point or 0 if the signal was not sent yet.

## Availability

| Up to Version |
|---|
