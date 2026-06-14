# Iso11783IL_GetWSMaster

> Category: `ISO11783` | Type: `function`

## Syntax

```c
dword Iso11783IL_GetWSMaster(dword ecuAddress);
```

## Description

This function returns the address of the Working Set Master, which is assigned to an ECU with the address ecuAddress.

## Return Values

address of the Working Set Master

## Example

```c
wsmAddr = Iso11783IL_GetWSMaster( 10 );
```

## Availability

| Since Version |
|---|
