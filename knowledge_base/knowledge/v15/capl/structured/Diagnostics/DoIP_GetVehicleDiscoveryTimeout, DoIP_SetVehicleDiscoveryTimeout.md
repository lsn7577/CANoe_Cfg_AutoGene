# DoIP_GetVehicleDiscoveryTimeout, DoIP_SetVehicleDiscoveryTimeout

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_SetVehicleDiscoveryTimeout(dword toVehicleDiscovery); // form 1
dword DoIP_GetVehicleDiscoveryTimeout(); // form 2
```

## Description

Sets or returns the timeout waiting for Vehicle Identification Response Messages after a Vehicle Identification Request was sent (in milliseconds).

## Parameters

| Name | Description |
|---|---|
| toVehicleDiscovery | Time in milliseconds [ms] |

## Example

This value can also be configured in the DoIP.INI file.

```c
// Wait longer than the standard suggests to detect more vehicles
DoIP_SetVehicleDiscoveryTimeout( 10000);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.1: form 1 8.1 SP4: form 2 | — | — | — | 1.0: form 1 1.0 SP2: form 2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
