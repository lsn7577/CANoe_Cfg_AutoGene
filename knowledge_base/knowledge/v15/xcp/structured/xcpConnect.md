# xcpConnect

> Category: `XCP` | Type: `function`

## Syntax

```c
void OnXcpConnect(char ecuQualifier[]);
```

## Description

Establishes a connection to the XCP/CCP device and starts the configured DAQ measurement.

If the connection is successfully depends on the response of the device.

Use xcpIsConnected to be aware of the connection.

After establishing the connection and before start of the DAQ measurement the callback function OnXcpConnect is called.

## Parameters

| Name | Description |
|---|---|
| ecuQualifier | Name of the device – configured within the CANoeXCP/CCP Window. |

## Example

```c
testcase TC_ConnectToECU ()
{
  xcpConnect("ECU");
....
}

//Callback function:
void OnXcpConnect (char ecuQualifier[])
{
  //Set calibration page to RAM
  xcpSetCalPage(ecuQualifier, 0x83, 0, 0);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.2: form 1 8.1: Callback | 13.0 | — | — | 1.0 |
| Restricted To | — | XCP | XCP | — | — | XCP |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
