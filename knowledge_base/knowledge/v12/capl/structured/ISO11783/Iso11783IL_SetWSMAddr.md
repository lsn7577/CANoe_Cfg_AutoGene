# Iso11783IL_SetWSMAddr

> Category: `ISO11783` | Type: `function`

## Syntax

```c
dword Iso11783IL_SetWSMAddr(dword wsmAddress);
```

## Description

Use this function to set the address of the Working Set Master, if this ECU is a member of a working set. All parameter groups which are addressed to the Working Set Master are also received by an ECU which calls this function.

## Return Values

0 on success or error code

## Example

```c
Iso11783IL_SetWSMAddr(0x06 );
```

## Availability

| Since Version |
|---|
