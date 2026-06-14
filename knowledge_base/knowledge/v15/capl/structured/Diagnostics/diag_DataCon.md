# diag_DataCon

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void diag_DataCon (long count); // form 1
void diag_DataCon (char target[], dword count); // form 2
```

## Description

Tells the diagnostic layer, via the count parameter, how many bytes of data were transmitted successfully.

This function is typically called within a transport layer callback. Once the diagnostic layer has initiated the transmission of a message via _Diag_DataRequest and the transport layer has sent this message in its entirety, using several message segments if needed, the diagnostic layer transport layer uses this function to indicate that the message was sent successfully.

## Parameters

| Name | Description |
|---|---|
| count | Number of bytes transmitted successfully. |
| target | The qualifier of the ECU the request was sent to. |

## Return Values

Error code

## Example

See DoIP_DataCon

```c
// This callback shall be called by an example TP layer
TPLayer_SendConfirmation( long connectionHandle, long count)
{
  char ecuQualifier[20];
  TPLayerGetECUQualifierForHandle(connectionHandle, ecuQualifier);
  diag_DataCon(ecuQualifier, count);
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
