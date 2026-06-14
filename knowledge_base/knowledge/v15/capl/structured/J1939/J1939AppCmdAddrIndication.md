# J1939AppCmdAddrIndication

> Category: `J1939` | Type: `function`

## Syntax

```c
dword J1939AppCmdAddrIndication( long ecuHandle, long length );
```

## Description

This function indicates that a new address has been assigned to the control device by the "CommandedAddress". The ECU must log on to the bus with the assigned address (see J1939ECUGoOnline()).

Since the PG also returns the name of the ECU, the data must be requested within this callback with J1939GetRxData(). This function is only called, if the ECU can change its address (‚Self Configuring Address‘-Bit of the device name must be set).

## Parameters

| Name | Description |
|---|---|
| ecuHandle | ECU handle |
| length | number of received data bytes |

## Return Values

—

## Example

```c
dword J1939AppCmdAddrIndication( LONG ecuHandle, LONG length)
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
