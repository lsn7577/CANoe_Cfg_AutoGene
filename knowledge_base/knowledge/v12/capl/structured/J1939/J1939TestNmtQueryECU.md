# J1939TestNmtQueryECU

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939TestNmtQueryECU( dword address );
```

## Description

The function queries for an ECU handle.

## Return Values

—

## Example

```c
LONG ecuHandle;

J1939TestNmtRefresh( 250 );
ecuHandle = J1939TestNmtQueryECU( 1 );

if (ecuHandle > 0) {
  address = J1939TestNmtQueryAddress( ecuHandle );
}
```

## Availability

| Since Version |
|---|
