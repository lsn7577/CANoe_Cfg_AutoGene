# Iso11783GetWSMaster

> Category: `ISO11783` | Type: `function`

## Syntax

```c
dword Iso11783GetWSMaster(char busName[], dword ecuAddress);
```

## Description

This function returns the address of the Working Set Master, which is assigned to an ECU with the address ecuAddress.

## Return Values

Address of the Working Set Master

## Example

```c
wsmAddr = Iso11783GetWSMaster( "default", 10 );
```

## Availability

| Since Version |
|---|
