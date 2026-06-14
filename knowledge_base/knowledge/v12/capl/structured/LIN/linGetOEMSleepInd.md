# linGetOEMSleepInd

> Category: `LIN` | Type: `function`

## Syntax

```c
long linGetOEMSleepInd()
```

## Description

With this function it's possible to query the sleep indication bit of a Slave node.

Without parameter, the sleep indication bit of the calling slave is returned or zero if the caller is not a slave.

## Return Values

-1: Function call not allowed, execution failed or invalid slave name given.

## Availability

| Since Version |
|---|
