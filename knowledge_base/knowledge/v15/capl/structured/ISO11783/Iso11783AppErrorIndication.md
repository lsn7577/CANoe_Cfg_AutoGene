# Iso11783AppErrorIndication

> Category: `ISO11783` | Type: `function`

## Syntax

```c
dword Iso11783AppErrorIndication( long ecuHandle, long errorClass, long errorNumber, long addCode );
```

## Description

Indicates that errors have occurred during a transfer or else during the initialization of ECUs (for example timeout during the transport protocol). If an Address Claiming procedure has failed, that will also be reported by means of this function.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | ECU handle |
| errorClass | Error class |
| errorNumber | Error number |
| addCode | Additional error parameter, depends on the error number (i.e. the PGN) |

## Return Values

—

## Example

```c
dword Iso11783AppErrorIndication( 
 LONG ecuHdl, LONG errClass, LONG errNum, LONG addCode )
{
  /* user code */
  return 0;
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.1 | 13.0 | — | — | — |
| Restricted To | — | Iso11783 | Iso11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
