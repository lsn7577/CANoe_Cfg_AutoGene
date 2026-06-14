# DoIP_SetRoutingActivationOEMSpecific

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_SetRoutingActivationOEMSpecific(long sendOEMSpecific, dword OEMspecific);
```

## Description

Sets the OEM-specific parameters in the Routing Activation Request Message.

## Parameters

| Name | Description |
|---|---|
| sendOEMSpecific | 0: Do not send the OEM specific field (default)1: Send the given value in the OEM specific field |
| OEMspecific | Value to send if the OEM specific field is activated. |

## Return Values

—

## Example

The message can also be configured from the DoIP.INI file

```c
// Send a constant in the RAR message
DoIP_SetRoutingActivationOEMSpecific( 1, 0x31425927);
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
