# diagGetFunctionalGroupExt

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetFunctionalGroupExt ()
```

## Description

Returns the value of the "address extension" byte (extended address information for ISO TP "extended addressing mode").

If the functional group is not specified, the destination set with diagSetTarget is used.

## Return Values

-1: Extended addressing is not used.

## Availability

| Since Version |
|---|
