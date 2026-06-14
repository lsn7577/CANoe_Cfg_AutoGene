# DoIP_SetGatewayLogicalAddress

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_SetGatewayLogicalAddress(dword logicalAddress);
```

## Description

Sets the logical address of the gateway that responds to a vehicle announcement request.

## Parameters

| Name | Description |
|---|---|
| logicalAddress | 0: there is no gateway or gateway’s and target’s logical address are identical 1..65535: the gateway has the given logical address other: reserved |

## Return Values

—

## Example

```c
DoIP_SetVehicleLogicalAddress( 0x201);
DoIP_SetGatewayLogicalAddress( 0x100);
DoIP_ConnectToVehicle();
// if the gateway with logical address 0x0100 responds to the vehicle
// identification request, the connection can be made even though the ECU
// with logical address 0x0201 is the target of the communication
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 | — | — | — | 2.1 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
