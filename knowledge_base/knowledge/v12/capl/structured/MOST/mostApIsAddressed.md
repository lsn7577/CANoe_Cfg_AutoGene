# mostApIsAddressed

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostApIsAddressed(long fblockID, long instID)
```

## Description

mostApIsAddressed checks whether the functional MOST address {fblockID, instID} matches the CAPL node function blocks assigned via mostApRegister() or mostApRegisterEx(). The functional address is permitted to contain wildcard symbols.

This function can be used to determine whether an incoming command message is destined for the CAPL node.

## Return Values

1: If a MOST application simulated by this CAPL node is addressed.

## Availability

| Since Version |
|---|
