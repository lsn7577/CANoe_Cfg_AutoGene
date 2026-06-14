# linGetOEMWakeupInd

> Category: `LIN` | Type: `function`

## Syntax

```c
long linGetOEMWakeupInd()
```

## Description

With this function it's possible to query the wake-up indication bit of a Slave node.

Without parameter, the wake-up indication bit of the calling slave is returned or zero if the caller is not a slave node.

## Return Values

-1: Function call not allowed, execution failed or invalid slave name given.

## Availability

| Since Version |
|---|
