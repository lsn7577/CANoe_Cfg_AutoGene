# GNSSAppErrorIndication

> Category: `J1939` | Type: `function`

## Syntax

```c
void GNSSAppErrorIndication( long errNum, long errClass, long addInfo )
```

## Description

This function identifies errors that occurred during a transfer or else during the initialization of the node (for example timeout during the transport protocol). If an Address Claiming procedure has failed, that will also be reported by means of this function.

The error classes and error codes are described here.

## Parameters

| Name | Description |
|---|---|
| errNum | Error number |
| errClass | Error class |
| addInfo | Additional error information |

## Return Values

—

## Example

```c
void GNSSAppErrorIndication( LONG errorClass, LONG errorCode, LONG addInfo )
{
  write( „Error code = %d“,errCode);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.2 | 13.0 | — | — | — |
| Restricted To | — | J1939 ISO11783 | J1939 ISO11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
