# J1939GetBus

> Category: `J1939` | Type: `function`

## Syntax

```c
dword J1939GetBus( char[] busName );
```

## Description

This function returns a bus handle.

## Return Values

bus handle or 0 if bus name is unknown

## Example

```c
dword busHandle;

busHandle = ( "ImplementBus 
 " );
J1939GetBus( busHandle);
```

## Availability

| Since Version |
|---|
