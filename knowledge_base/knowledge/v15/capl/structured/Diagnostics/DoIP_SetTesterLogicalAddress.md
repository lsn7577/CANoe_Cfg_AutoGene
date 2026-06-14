# DoIP_SetTesterLogicalAddress

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_SetTesterLogicalAddress(dword logicalAddress);
```

## Description

Sets logical DoIP address of the tester used for sending.

Note that ECU simulations will typically send responses to the tester address received in requests.

## Parameters

| Name | Description |
|---|---|
| logicalAddress | Address used (0x0000 to 0xFFFF) |

## Return Values

—

## Example

```c
DoIP_SetTesterLogicalAddress( 0x1000);
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
