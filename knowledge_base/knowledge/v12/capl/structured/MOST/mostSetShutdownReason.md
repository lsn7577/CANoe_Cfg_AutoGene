# mostSetShutdownReason

> Category: `MOST` | Type: `function`

## Syntax

```c
mostSetShutdownReason(long channel, long reason)
```

## Description

Sets the shutdown reason value. This function is needed for resetting the shutdown reason value to 0x00 (No result available).

It is recommended to call this function from the OnMostShutdownReason event procedure.

## Return Values

<0: See error codes

## Availability

| Since Version |
|---|
