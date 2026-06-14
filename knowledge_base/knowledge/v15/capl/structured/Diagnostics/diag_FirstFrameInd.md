# diag_FirstFrameInd

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void diag_FirstFrameInd(long source, long target, long length); // form 1
void diag_FirstFrameInd(char ecuQualifier[], dword length); // form 2
```

## Description

Indicates the start of a diagnostic data reception to the diagnostic layer.

This function is typically called from a transport layer callback. For example, the ISO TP protocol on CAN indicates the reception of a First Frame to the application.

In the diagnostic layer of a tester, a call to this function will stop the timer started after the request has been sent, i.e. even a very long data reception will not time out. If the tester has called testWaitForDiagResponseStart, that call will now be continued.

## Parameters

| Name | Description |
|---|---|
| source | Identifies the sender node. |
| target | Identifies the receiver. |
| length | Number of bytes announced. |
| ecuQualifier | Qualifier of the ECU that has started to send a response. |

## Return Values

Error code

## Example

The OSEKTL API for the ISO TP on CAN implementation found in OSEK_TP.dll reports First Frames in the callback function OSEKTL_FirstFrameInd (see OSEK TP). The arguments can simply be forwarded in this case:

```c
OSEKTL_FirstFrameIndication( long source, long target, long length)
{
diag_FirstFrameInd(source, target, length);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.1: form 1 11.0: form 2 | — | — | — | 1.0: form 1 3.0: form 2 |
| Restricted To | — | Online mode | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
