# J1939TestChkCreate_PGDistanceViolation

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939TestChkCreate_PGDistanceViolation(dword refSource, dword refDest, dword refPgn, dword obsrvSource, dword obsrvDest, dword obsrvPgn, dword aMinDistance, dword aMaxDistance, char callback[] )
```

## Description

An event is generated if the time interval that starts on receipt of the reference message and ends with the receipt of the observed message is smaller than aMinDistance or is larger than aMaxDistance.

## Parameters

| Name | Description |
|---|---|
| refPgn | referenced parameter group number |
| refSource | referenced source address of the PG or Null Address (0xFE) for wildcard |
| refDest | referenced destination address of the PG or Null Address (0xFE) for wildcard, ignored for broadcast PGs |
| obsrvPgn | observed parameter group number |
| obsrvSource | observed source address of the PG or Null Address (0xFE) for wildcard, ignored for broadcast PGs |
| obsrvDest | observed destination address of the PG or Null Address (0xFE) for wildcard, ignored for broadcast PGs |
| aMinDistance | minimum allowed distance between PGs in milliseconds, 0 < x < aMaxDistance |
| aMaxDistance | maximum allowed distance between PGs in milliseconds, aMinCycleTime < x < MAX_dword |
| callback | name of the callback which is called when the check fails or 0, signature: void Callback( long checked ) |

## Example

```c
long distCheck ;
distCheck = J1939TestChkCreate_PGDistanceViolation( 1, 2, 0xf100, 2, 1, 0xf101, 80, 120, "PGDistanceCallback" );J1939TestChkControl_Start( distCheck );
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.1 | 13.0 | — | — | 1.1 SP2 |
| Restricted To | — | J1939 | J1939 | — | — | J1939 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
