# mostGetLockEx

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostGetLockEx (long channel)
```

## Description

The function returns the lock status of the connected MOST hardware. In contrast to mostGetLock(), the additional states "Stable Lock" and "Critical Unlock" are considered according to MOST specification 2.3.

## Return Values

0: Unlock

## Availability

| Since Version |
|---|
