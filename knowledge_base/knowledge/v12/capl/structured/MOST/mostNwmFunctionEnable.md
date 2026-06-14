# mostNwmFunctionEnable

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostNwmFunctionEnable(long functionId, long opTypes)
```

## Description

Registers and unregisters a function and its operations with the NetworkMaster.

The NetworkMaster will not response to the new registered function and thus an on mostMessage/on mostAMSMessge handler has to be implemented in the CAPL module of the NetworkMaster.

## Return Values

See error codes

## Availability

| Since Version |
|---|
