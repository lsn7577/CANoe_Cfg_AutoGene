# Iso11783GetBusName

> Category: `ISO11783` | Type: `function`

## Syntax

```c
dword Iso11783GetBusName( dword busHandle, dword bufferSize, char buffer[] );
```

## Description

Gets a bus name.

## Return Values

0 or error code

## Example

```c
char busName[32];
Iso11783GetBusName( busHandle, 
 elCount(busName), busName );
```

## Availability

| Since Version |
|---|
