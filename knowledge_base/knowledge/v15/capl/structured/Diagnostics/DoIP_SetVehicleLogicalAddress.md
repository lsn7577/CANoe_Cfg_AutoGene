# DoIP_SetVehicleLogicalAddress

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_SetVehicleLogicalAddress(dword logicalAddress);
```

## Description

Sets vehicle logical DoIP address sent in DoIP PDUs.

## Parameters

| Name | Description |
|---|---|
| logicalAddress | Address used (0x0000 to 0xFFFF) |

## Return Values

—

## Example

The following example sets the Logical Address of a vehicle (used e.g. in Routing Activation Responses) and makes it known to the DoIP layer.

```c
dword gGatewayLogAddress = 0x1000;
write("Logical address of vehicle = 0x%04x", gGatewayLogAddress);
DoIP_SetVehicleLogicalAddress( gGatewayLogAddress);
DoIP_AddECU( gGatewayLogAddress);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.1 SP2 | — | — | — | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
