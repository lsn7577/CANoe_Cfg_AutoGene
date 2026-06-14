# AfdxInitSchedule

> Category: `ADFX` | Type: `function`

## Syntax

```c
long AfdxInitSchedule( long packet );
```

## Description

Initializes the scheduled transmission of the specified message during the start phase of the measurement.

The behavior of the function call differs for different measurement phases.

## Parameters

| Name | Description |
|---|---|
| packet | Handle of the message that has been created with AfdxInitPacket. |

## Example

```c
on preStart
{
  long packet;
  char errTxt[256];

  packet = AfdxInitPacket(0, "TESTMSG_ALLTYPES", 0 );
  if (packet == 0)
  {
    AfdxGetLastErrorText(elCount(errTxt), errTxt);
    writeEx( -3, 0, "<%NODE_NAME%> AfdxInitPacket failed due to:%s", errTxt );
  }

  if (AfdxInitSchedule(packet) != 0)
  {
    AfdxGetLastErrorText(elCount(errTxt), errTxt);
    writeEx( -3, 0, "<%NODE_NAME%> AfdxInitSchedule failed due to:%s", errTxt );
  }
  AfdxReleasePacket(packet);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 SP3 | — | — | — | — |
| Restricted To | — | AFDX | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
