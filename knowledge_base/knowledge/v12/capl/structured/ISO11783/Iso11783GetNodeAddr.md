# Iso11783GetNodeAddr

> Category: `ISO11783` | Type: `function`

## Syntax

```c
dword Iso11783GetNodeAddr( dword ecuHandle );
```

## Description

This function returns the current address of a logical ECU.

## Return Values

Current ECU address
0xFE if the address is the ISO11783 NULL address. If this function is called with an invalid handle, the function returns 0xFFFF.

## Example

```c
addr = Iso11783GetNodeAddr(ecuHandle);
```

## Availability

| Since Version |
|---|
