# J1939GetWSMaster

> Category: `J1939` | Type: `function`

## Syntax

```c
dword J1939GetWSMaster(char busName[], dword ecuAddress)
```

## Description

This function returns the address of the Working Set Master, which is assigned to an ECU with the address ecuAddress.

## Return Values

address of the Working Set Master

## Example

```c
wsmAddr = J1939GetWSMaster( "default", 10 );
```

## Availability

| Since Version |
|---|
