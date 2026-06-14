# Iso11783GetWSMAddr

> Category: `ISO11783` | Type: `function`

## Syntax

```c
dword Iso11783GetWSMAddr( dword ecuHandle );
```

## Description

This function returns the address of the Working Set Master, which is assigned to this ECU.

## Return Values

Address of the Working Set Master for this ECU or the Null-Address (0xFE)

## Example

```c
addr = Iso11783GetWSMAddr( ecuHdl );
```

## Availability

| Since Version |
|---|
