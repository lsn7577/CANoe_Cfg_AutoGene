# _DoIP_RoutingActivationRequest

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long _DoIP_RoutingActivationRequest(dword sourceAddress, dword activationType, dword reserved, dword OEM, BYTE sendResponse[], BYTE responseCodeOut[]);
```

## Description

A request for routing activation was received in a vehicle simulation. It is possible to ignore, accept or deny the request, and to specify if a response message is sent.

## Parameters

| Name | Description |
|---|---|
| sourceAddress | Logical address of the tester that sent the request. |
| activationType | The tester has requested this type of connection, e.g. WWH-OBD or default. |
| reserved | The value of the reserved field in the request message. |
| OEM | The value of the OEM field in the request, or 0, if field is not present. |
| sendResponse | Output parameter to indicate whether the simulation shall send a routing activation response message: 0: Do not send a response message 1: Send a response message other: reserved |
| responseCodeOut | If a response is sent, this value will be used as response code. |

## Example

```c
long _DoIP_RoutingActivationRequest(dword sourceAddress, dword activationType,dword reserved, dword OEM, BYTE sendResponse[], BYTE responseCodeOut[])
{
  write("_DoIP_RoutingActivationRequest(%04x, 0x%02x, reserved=%08x, OEM=%08x)"
  , sourceAddress, activationType, reserved, OEM);
  // sendResponse[0]    is always 1    (default: send response)
  // responseCodeOut[0] is always 0x10

  // Accept default or WWH-OBD
  if(activationType <= 0x01)
    return 0;  // continue with default behavior

  // Ignore a specific activation type, i.e. do not even send a response
  if(activationType == 0x99)
  {
    sendResponse[0] = 0;
    return 1;  // deny routing activation
  }

  // Accept a specific activation type only if reserved value is correct
  if(IsValidForActivationType( activationType, reserved))
    return 2;  // allow routing activation

  // All other activation types shall be denied
  responseCodeOut[0] = 0x06; // UnsupportedActivationType
  return 1; // deny routing activation
}
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
