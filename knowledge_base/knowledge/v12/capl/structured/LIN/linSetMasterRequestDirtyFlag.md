# linSetMasterRequestDirtyFlag

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linSetMasterRequestDirtyFlag (dword dirty)
```

## Description

Sets the dirty flag for the LIN master request frame (frame identifier=0x3C). The master request only gets transmitted when the dirty flag is set.

The dirty flag also gets set implicitly with every data update on the master request.

## Return Values

On success, a value unequal to zero, otherwise zero.

## Availability

| Since Version |
|---|
