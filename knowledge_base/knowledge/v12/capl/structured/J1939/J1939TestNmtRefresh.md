# J1939TestNmtRefresh

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939TestNmtRefresh( dword waitTime );
```

## Description

Sends a ‘Request for Address Claim’ from Null Address (0xFE) and updates the NMT table. The function waits until the specified time is elapsed.

## Example

```c
char deviceName[8];
J1939TestNmtRefresh( 250 );
J1939TestNmtQueryDeviceName( 1, deviceName );
```

## Availability

| Since Version |
|---|
