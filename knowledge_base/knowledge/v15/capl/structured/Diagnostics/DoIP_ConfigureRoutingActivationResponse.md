# DoIP_ConfigureRoutingActivationResponse

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_ConfigureRoutingActivationResponse(dword valueReserved);
```

## Description

Configures the routing activation response message sent by the vehicle simulation on the reception of a routing activation request message.

## Parameters

| Name | Description |
|---|---|
| valueReserved | The value of the reserved field in the message. ISO 13400 specifies a default value of 0x00000000. |

## Return Values

—

## Example

```c
// Set the reserved field in the routing activation response message to 0x12345678
DoIP_ConfigureRoutingActivationResponse(0x12345678);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 10.0 SP3 | — | — | — | 2.2 SP3 |
| Restricted To | — | Test Nodes | — | — | — | Test Nodes |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
