# InterfaceStatus

> Category: `Other` | Type: `function`

## Syntax

```c
void InterfaceStatus(long time, long channel, long status);
```

## Description

The callback can be inserted in the sections callback function or function.

The callback occurs when the status of the connection to the interface hardware is changed (e.g. when Windows reports a lost connection to a CAN/WLAN gateway or to a WLAN interface hardware for Car2x communication).

## Parameters

| Name | Description |
|---|---|
| time | Time, resolution 10us |
| channel | The channel number |
| status | Status of the channel Values:3015: The connection is lost |

## Return Values

—

## Example

```c
void InterfaceStatus(long time, long channel, long status)
{
   if(status == 3015)
   {
      write("Time %f s, channel %d: The connection to the interface is lost!", ((float)time)/100000.0, channel);
   }
   else
   {
      //other status is not yet supported
   }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.6 | 7.6 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | ✔ | N/A |
