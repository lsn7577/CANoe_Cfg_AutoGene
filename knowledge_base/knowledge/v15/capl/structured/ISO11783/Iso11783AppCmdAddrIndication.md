# Iso11783AppCmdAddrIndication

> Category: `ISO11783` | Type: `function`

## Syntax

```c
dword Iso11783AppCmdAddrIndication( long ecuHandle, long length );
```

## Description

This function indicates that a new address has been assigned to the control device by the "CommandedAddress". The ECU must log on to the bus with the assigned address (see Iso11783ECUGoOnline()).

Since the PG also returns the name of the ECU, the data must be requested within this callback with Iso11783GetRxData(). This function is only called, if the ECU can change its address (‚Self Configuring Address‘-Bit of the device name must be set).

## Parameters

| Name | Description |
|---|---|
| ecuHandle | ECU handle |
| length | Number of received data bytes |

## Return Values

—

## Example

```c
dword Iso11783AppCmdAddrIndication( LONG ecuHandle, LONG length)
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
