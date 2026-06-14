# mostGetNceType

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostGetNceType()
```

## Description

Returns the type of network change event (NCE) (when changing the MPR register).

This function can only be called within the OnMostMPR() event procedure.

## Return Values

< 0: NCE-. The absolute value corresponds to the number of devices which closed their bypass.

## Availability

| Since Version |
|---|
