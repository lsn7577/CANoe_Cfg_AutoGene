# diag_ErrorInd

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void diag_ErrorInd (long error); // form 1
void diag_ErrorInd (char target[], long error); // form 2
```

## Description

Reports errors to the diagnostic layer.

This function is typically called within a transport layer callback. The transport layer uses it to report errors to the diagnostic layer.

If, for example, testWaitForDiagResponse is used in a test module to wait for receipt of a response and Diag_ErrorInd reports an error, the test function returns an error and stops waiting.

## Parameters

| Name | Description |
|---|---|
| error | Error number. This number is valid only in the context of the concrete transport protocol implementation used. It is recommended to forward error numbers reported by the protocol layer. For example, the OSEKTL API for the ISO TP on CAN implementation found in OSEK_TP.DLL reports errors in the callback function OSEKTL_ErrorInd (see OSEK TP). The error number reported here can simply be forwarded to the diagnostic layer: OSEKTL_ErrorInd( int error) { diag_ErrorInd( error);} |
| target | Qualifier of the ECU for which there was a communication error. |

## Return Values

Error code

## Example

See DoIP_ErrorInd

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
