# _Diag_DataRequest

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void _Diag_DataRequest (BYTE data[], dword count, long furtherSegments);
```

## Description

With this function CANoe triggers the CAPL interface to transmit data.

## Parameters

| Name | Description |
|---|---|
| data | The data of the diagnostic primitive (byte stream of request or response) that the node should transmit on the bus. This may be several hundred or thousand bytes, therefore a suitable transport protocol has to be used here to forward the data. |
| count | The actual number of bytes to be sent. |
| 0 | This is the last segment of a segmented transmission (see diag_SetDataSegmentation), typical value for ISO TP. |
| 1 | Further segments follow. |
| other | reserved |

## Return Values

—

## Example

See DoIP_DataReq

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.1 | — | — | — | 1.0 |
| Restricted To | — | Online mode | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
