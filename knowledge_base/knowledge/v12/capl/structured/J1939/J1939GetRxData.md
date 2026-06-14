# J1939GetRxData

> Category: `J1939` | Type: `function`

## Syntax

```c
dword J1939GetRxData( dword bufferSize, char buffer[] );
```

## Description

An auxiliary function for receiving PG data within a callback function.

The DLL interface will not permit you to transfer data arrays via callback. Therefore it serves the purpose of "retrieving" data from the node layer. Since this function is called within a callback, there is no need to transfer an ECU handle. If the function is called from outside of a callback, the call has no effect.

## Return Values

number of bytes copied

## Example

```c
char data[100];
dword count;

count = J1939GetRxData( elCount(data), data );
```

## Availability

| Since Version |
|---|
