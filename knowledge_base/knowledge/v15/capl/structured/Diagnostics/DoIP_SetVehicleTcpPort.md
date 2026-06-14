# DoIP_SetVehicleTcpPort

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_SetVehicleTcpPort( dword port);
```

## Description

Sets the TCP port (TCP_DATA) to be used by the DoIP layer.

This function must be called in on preStart.

## Parameters

| Name | Description |
|---|---|
| port | The TCP_DATA port of the DoIP layer. |

## Return Values

—

## Example

```c
dword port;
port = DiagGetCommParameter( "DoIP.VEHICLE_TCP_Data");
// Set the vehicle TCP port
DoIP_SetVehicleTcpPort( port);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.1 SP4 | — | — | — | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
