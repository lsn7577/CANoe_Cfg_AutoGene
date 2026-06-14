# diag_DataInd

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void diag_DataInd (byte rxBuffer [], long count, long sender); // form 1
void diag_DataInd (char target[], byte rxBuffer[], dword count); // form 2
```

## Description

Passes count bytes of the transmitter address sender from the rxBuffer buffer to the diagnostic layer.

Alternatively, the transmitter can be identified using its ECU qualifier target.

This function is typically called in a transport layer callback after a message, which may be segmented, has been received in its entirety. The transport layer removes all protocol information (segmentation, flow control, etc.) and forwards only the payload data (e.g. the ECU diagnostic response starting at the service ID and including all response parameters) to the diagnostic layer.

## Parameters

| Name | Description |
|---|---|
| rxBuffer | Byte buffer to be passed to the diagnostic layer. |
| sender | Address of the transmitter from which the diagnostic message was received. |
| count | Number of bytes to be passed. |
| target | Qualifier of the responding ECU. |

## Return Values

Error code

## Example

See DoIP_DataInd

```c
// This callback shall be called by an example TP layer
TPLayer_ReceivedData( long connectionHandle, byte data[])
{
  char ecuQualifier[20];
  TPLayerGetECUQualifierForHandle(connectionHandle, ecuQualifier);
  diag_DataInd(ecuQualifier, data, elcount(data));
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.0: form 1 11.0: form 2 | — | — | — | 1.0: form 1 3.0: form 2 |
| Restricted To | — | Online mode | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
