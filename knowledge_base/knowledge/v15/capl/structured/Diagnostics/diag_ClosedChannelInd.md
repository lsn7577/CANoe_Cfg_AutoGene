# diag_ClosedChannelInd

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diag_ClosedChannelInd (); // form 1
long diag_ClosedChannelInd (char target[]); // form 2
```

## Description

This function communicates to CANoe that the communication channel is not longer available, e.g. the tester closed the channel or a non reparable error occurred.

The CAPL program first has to call diag_SetupChannelCon before further data can be sent.

## Parameters

| Name | Description |
|---|---|
| target | The qualifier of the ECU whose channel has been closed. |

## Return Values

Error code

## Example

```c
// This callback shall be called by an example TP layer
	TPLayer_ClosedChannel( long connectionHandle)
{
   char ecuQualifier[20];
  TPLayerGetECUQualifierForHandle(connectionHandle, ecuQualifier);
  diag_ClosedChannelInd(ecuQualifier);
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
