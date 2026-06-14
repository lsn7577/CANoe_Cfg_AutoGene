# Iso11783IL_GetWSMAddr

> Category: `ISO11783` | Type: `function`

## Syntax

```c
dword Iso11783IL_GetWSMAddr();
```

## Description

This function returns the address of the Working Set Master, which is assigned to this ECU.

## Return Values

address of the Working Set Master for this ECU or the Null-Address (0xFE)

## Example

```c
addr = Iso11783IL_GetWSMAddr();
```

## Availability

| Since Version |
|---|
