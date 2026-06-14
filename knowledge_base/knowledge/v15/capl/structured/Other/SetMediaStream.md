# SetMediaStream

> Category: `Other` | Type: `function`

## Syntax

```c
SetMediaStream(panel, control, busType, channel, streamIndex, streamId[]);
```

## Description

Replaces the media stream at the specified index of the Panel Designer during runtime:

Media Stream Control

The panel is accessed by its individual panel name that is entered in the Panel Designer.

## Parameters

| Name | Description |
|---|---|
| panel | Panel name, restricted to 128 characters."" – references all loaded panelsIf you open a panel the first time, the panel is loaded. If you close the panel, it remains loaded. |
| control | Name of the control, restricted to 128 characters."" – references all controls on the panel. |
| busType | Bus type of the source media stream (e.g. eCAN, eFlexRay, eEthernet, ...).Currently only bus type eEthernet is supported. |
| channel | Channel number of the source media stream. |
| streamIndex | Target stream index of the Media Stream Control. |
| streamId | Stream ID of the source media stream. |

## Return Values

—

## Example

Setting media stream from Ethernet channel 1.

```c
on key 'x'
{
  byte streamId[8] = { 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x00, 0x01 };
  SetMediaStream("AVTP Video H.264", "Media Stream Control", eEthernet, 1, 0, streamId);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 11.0 | 11.0 | 13.0 | — | 14 | 3.0 |
| Restricted To | Media Stream Control | Media Stream Control | Media Stream Control | — | Media Stream Control | Media Stream Control |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | ✔ | N/A |
