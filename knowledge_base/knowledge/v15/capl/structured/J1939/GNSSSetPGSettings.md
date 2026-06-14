# GNSSSetPGSettings

> Category: `J1939` | Type: `function`

## Syntax

```c
dword GNSSSetPGSettings( dword pgn, dword enable, dword destination, dword priority, dword updateRate )
```

## Description

This function can be used to change the values of individual parameter groups. So far, the NMEA 2000® parameter groups “GNSS Position Data” (PGN 129029), “Position Delta, High Precision Rapid Update” (PGN 129027), “Position, Rapid Update” (PGN 129025), and “COG & SOG, Rapid Update” (PGN 129026) as well as the J1939 parameter groups "VehiclePosition" (PGN 65267) and “Vehicle Direction/Speed” (PGN 65256) are supported.

By default “Vehicle Direction/Speed” is not transmitted cyclically. But if enabled this message can be requested by a request message.

When a node is reached with GNSSStartUp, the following start values are set:

Thus the first both parameter groups are transferred if this function is not called.

The function is only performed successfully if the simulation has not yet been started.

## Parameters

| Name | Description |
|---|---|
| pgn | number of the parameter group |
| enable | 1 if this parameter group should be sent, otherwise 0 |
| destination | target address of the parameter group |
| priority | priority of the parameter group |
| updateRate | time interval in milliseconds at which the parameter group is sent |

## Return Values

error code

## Example

```c
// disable PG “Position, Rapid Update”
GNSSSetPGSettings( 129025, 0, 255, 3, 1000 );
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.2 | 13.0 | — | — | — |
| Restricted To | — | J1939 ISO11783 | J1939 ISO11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
