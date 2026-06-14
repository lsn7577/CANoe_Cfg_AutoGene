# DoIP_ConfigureRoutingActivationRequest

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_ConfigureRoutingActivationRequest(long mode, dword activationType, dword valueReserved);
```

## Description

Configures the Routing Activation Request Message sent by a tester.

## Parameters

| Name | Description |
|---|---|
| mode | 0: Do not send a routing activation type1: Send 1 byte activation type, value must be <= 0xFF (default)2: Send 2 byte activation type, value must be <= 0xFFFF |
| activationType | The value to send if an activation type is configured (i.e. mode is equal to 1 or 2). |
| valueReserved | The value of the reserved field in the message. |

## Return Values

—

## Example

You can also configure these values in the DoIP.INI file.

```c
// Send the 2 byte activation type 0x1234, and set the reserved field
DoIP_ConfigureRoutingActivationRequest( 2, 0x1234, 0x76543210);
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
