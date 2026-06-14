# DoIP_ConfigureVehicleAnnouncement

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_ConfigureVehicleAnnouncement(dword toInitial_ms, dword messageCount, dword toInterval_ms);
```

## Description

Configures when the Vehicle Announcement Messages are sent.

## Parameters

| Name | Description |
|---|---|
| Note This parameter is ignored, if the function DoIP_AnnounceVehicle is used for sending Vehicle Announcement Messages. |  |
| messageCount | Number of announcement messages sent when the measurement starts, or DoIP_AnnounceVehicle is called. |
| toInterval_ms | Time between the announcement messages when more than 1 is configured. |

## Return Values

—

## Example

```c
// Send 5 announcement messages after 200 ms, with 100 ms interval
DoIP_ConfigureVehicleAnnouncement( 200, 5, 100);
DoIP_AnnounceVehicle();
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.1 SP4 | — | — | — | 1.0 SP2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
