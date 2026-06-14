# frGetFrameCRC

> Category: `FlexRay` | Type: `function`

## Syntax

```c
dword frGetFrameCRC(this);
```

## Description

This function returns the CRC of a received FlexRay frame.

The Header CRC can be determined with a special selector of the event procedure.

## Parameters

| Name | Description |
|---|---|
| this | The function can only be used in the context of the following event procedures: on frRSlot on frFrame on frNullFrame on frFrameError this references the corresponding receive object in the event procedure. |

## Example

The following example writes the CRC into the Write Window for all received frames.

```c
on frFrame *
{
   dword 
 crc;
   crc 
 = frGetFrameCRC(this);
   Write(“Frame %d in Cycle %d has CRC 0x%x”, this.FR_SlotID, this.FR_Cycle, crc);
   output(this); // only required in Measurement Setup
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 6.1 | 6.1 | 13.0 | — | — | 1.0 |
| Restricted To | FlexRay | FlexRay | FlexRay | — | — | FlexRay |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
