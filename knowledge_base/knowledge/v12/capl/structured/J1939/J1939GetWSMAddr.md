# J1939GetWSMAddr

> Category: `J1939` | Type: `function`

## Syntax

```c
dword J1939GetWSMAddr( dword ecuHandle );
```

## Description

This function returns the address of the Working Set Master, which is assigned to this ECU.

## Return Values

address of the Working Set Master for this ECU or the Null-Address (0xFE)

## Example

```c
addr = J1939GetWSMAddr( ecuHdl );
```

## Availability

| Since Version |
|---|
