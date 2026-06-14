# J1939SetWSMAddr

> Category: `J1939` | Type: `function`

## Syntax

```c
dword J1939SetWSMAddr( dword ecuHandle, dword wsmAddress );
```

## Description

Use this function to set the address of the Working Set Master, if this ECU is a member of a working set. All parameter groups which are addressed to the Working Set Master are also received by an ECU which calls this function.

## Return Values

0 on success or error code

## Example

```c
J1939SetWSMAddr( ecuHdl, 0x06 );
```

## Availability

| Since Version |
|---|
