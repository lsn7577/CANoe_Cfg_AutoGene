# linGetOEMDataInd

> Category: `LIN` | Type: `function`

## Syntax

```c
long linGetOEMDataInd()
```

## Description

With this function it's possible to query the data indication bit of a Slave node.

Without parameter, the data indication bit of the calling slave node is returned or zero if the caller is not a slave node.

## Return Values

-1: Function call not allowed, execution failed or invalid slave name given.

## Availability

| Since Version |
|---|
