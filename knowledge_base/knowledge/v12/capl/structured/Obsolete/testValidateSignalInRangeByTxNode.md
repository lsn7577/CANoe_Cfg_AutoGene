# testValidateSignalInRangeByTxNode

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long testValidateSignalInRangeByTxNode (char aTestStep[], dbSignal aSignal, dbNode aTxNode, float aLowLimit, float aHighLimit)
```

## Description

Checks the signal value against the condition:

aLowLimit <= Value <= aHighLimit

The test step is then evaluated as passed or failed, depending on the results

## Return Values

-1: General error

## Availability

| Since Version |
|---|
