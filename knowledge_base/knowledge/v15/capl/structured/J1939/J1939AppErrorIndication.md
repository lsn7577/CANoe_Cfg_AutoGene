# J1939AppErrorIndication

> Category: `J1939` | Type: `function`

## Syntax

```c
dword J1939AppErrorIndication( long ecuHandle, long errorClass, long errorNumber, long addCode );
```

## Description

Indicates that errors have occurred during a transfer or else during the initialization of ECUs (for example timeout during the transport protocol). If an Address Claiming procedure has failed, that will also be reported by means of this function.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | ECU handle |
| errorClass | error class |
| errorNumber | error number |
| addCode | additional error parameter, depends on the error number (i.e. the PGN) |

## Return Values

—

## Example

```c
dword J1939AppErrorIndication( LONG ecuHdl, LONG errClass, LONG errNum, LONG addCode )
{
  /* user code */
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.1 | 13.0 | — | — | — |
| Restricted To | — | J1939 | J1939 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
