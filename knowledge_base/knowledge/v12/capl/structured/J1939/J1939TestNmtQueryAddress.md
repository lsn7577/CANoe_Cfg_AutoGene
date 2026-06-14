# J1939TestNmtQueryAddress

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939TestNmtQueryAddress( long ecuHandle );
```

## Description

The function queries for an ECU address.

## Example

```c
char deviceName[8];
J1939TestNmtRefresh( 250 );
address = J1939TestNmtQueryAddress( deviceName, 0x12 );
```

## Availability

| Since Version |
|---|
