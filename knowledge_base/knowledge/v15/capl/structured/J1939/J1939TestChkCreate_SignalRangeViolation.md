# J1939TestChkCreate_SignalRangeViolation

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939TestChkCreate_SignalRangeViolation( dword sourceAddr, dword destAddr, dbMsg msg, dbSignal signal, float minSignalValue, float maxSignalValue, char callback[] )
```

## Description

Checks the value of a signal. The given interval (inclusive the limits) should be never left. An event will be generated, if the physical signal value lies outside the given value interval.

## Parameters

| Name | Description |
|---|---|
| msg | message from database |
| sourceAddr | source address of the PG or Null Address (0xFE) for wildcard |
| destAddr | destination address of the PG or Null Address (0xFE) for wildcard, ignored for broadcast PGs |
| signal | signal from database, which should be observed |
| minSignalValue | minimum limit of the signal range, 0 < x < maxSignalValue |
| maxSignalValue | maximum limit of the signal range, minSignalValue < x < MAX_FLOAT |
| callback | name of the callback, which is called when the check fails or 0, signature: void Callback( long checked ) |

## Example

```c
long signalCheck;
signalCheck = J1939TestChkCreate_SignalRangeViolation( 1, 2, EngineData, EngineData::Speed, 0.0, 2000.0,"SignalCallback" );
J1939TestChkControl_Start(signalCheck);
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
