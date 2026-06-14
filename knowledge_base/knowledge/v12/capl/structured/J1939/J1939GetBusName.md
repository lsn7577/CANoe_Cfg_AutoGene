# J1939GetBusName

> Category: `J1939` | Type: `function`

## Syntax

```c
dword J1939GetBusName( dword busHandle, dword bufferSize, char buffer[] );
```

## Description

Gets a bus name.

## Example

```c
char busName[32];
J1939GetBusName( busHandle, 
 elCount(busName), busName );
```

## Availability

| Since Version |
|---|
