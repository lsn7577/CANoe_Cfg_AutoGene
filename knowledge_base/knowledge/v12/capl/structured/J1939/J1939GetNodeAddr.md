# J1939GetNodeAddr

> Category: `J1939` | Type: `function`

## Syntax

```c
dword J1939GetNodeAddr( dword ecuHandle );
```

## Description

This function returns the current address of a logical ECU.

## Return Values

current ECU address
0xFE if the address is the J1939 NULL address. If this function is called with an invalid handle, the function returns 0xFFFF.

## Example

```c
addr = J1939GetNodeAddr(ecuHandle);
```

## Availability

| Since Version |
|---|
