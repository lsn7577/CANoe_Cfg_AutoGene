# J1939TestNmtQueryDeviceName

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939TestNmtQueryDeviceName( long ecuHandle, char retDeviceName[8] );
```

## Description

The function queries for an ECU device name.

## Example

```c
char deviceName[8];
J1939TestNmtRefresh( 250 );
J1939TestNmtQueryDeviceName( 1, deviceName );
```

## Availability

| Since Version |
|---|
