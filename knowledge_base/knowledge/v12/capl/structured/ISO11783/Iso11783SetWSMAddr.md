# Iso11783SetWSMAddr

> Category: `ISO11783` | Type: `function`

## Syntax

```c
dword Iso11783SetWSMAddr( dword ecuHandle, dword wsmAddress );
```

## Description

Use this function to set the address of the Working Set Master, if this ECU is a member of a working set. All parameter groups which are addressed to the Working Set Master are also received by an ECU which calls this function.

## Return Values

0 on success or error code

## Example

```c
Iso11783SetWSMAddr( ecuHdl, 0x06 );
```

## Availability

| Since Version |
|---|
