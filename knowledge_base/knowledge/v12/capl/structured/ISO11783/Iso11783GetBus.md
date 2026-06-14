# Iso11783GetBus

> Category: `ISO11783` | Type: `function`

## Syntax

```c
dword Iso11783GetBus( char[] busName );
```

## Description

This function returns a bus handle.

## Return Values

Bus handle or 0 if bus name is unknown

## Example

```c
dword busHandle;

busHandle = ( "ImplementBus 
 " );
Iso11783GetBus( busHandle);
```

## Availability

| Since Version |
|---|
