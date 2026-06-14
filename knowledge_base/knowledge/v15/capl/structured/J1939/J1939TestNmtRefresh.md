# J1939TestNmtRefresh

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939TestNmtRefresh( dword waitTime );
```

## Description

Sends a ‘Request for Address Claim’ from Null Address (0xFE) and updates the NMT table. The function waits until the specified time is elapsed.

## Parameters

| Name | Description |
|---|---|
| waitTime | wait until this time elapses, in milliseconds |

## Example

```c
char deviceName[8];
J1939TestNmtRefresh( 250 );
J1939TestNmtQueryDeviceName( 1, deviceName );
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
