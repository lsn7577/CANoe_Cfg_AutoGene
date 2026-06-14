# xcpSetCalPage

> Category: `XCP` | Type: `function`

## Syntax

```c
void OnXcpSetCalPage(char ecuQualifier[]);
```

## Description

If the XCP slave device supports calibration data page switching, this command sets the current page and access mode.

The callback returns that the ECU switched the calibration data page.

## Parameters

| Name | Description |
|---|---|
| ecuQualifier | Name of the device, configured within the CANoeXCP/CCP Window. |
| Bit 7 | Use for all segments, i.e. parameter segmentNr is ignored. |
| Bit 1 | The slave device XCP driver will access the given page. |
| Bit 0 | The given page will be used by the slave device application. |
| segmentNr | Logical data segment number. Ignored if bit 7 of the mode parameter is set to 1. |
| pageNr | Logical data page number. Usually 0 identifies the page in RAM and 1 the page in FLASH memory. CANoe.XCP can only work on parameters stored in RAM. |

## Return Values

—

## Example

```c
variables
{
   long mMode;
   long mSegmentNr;
}

void OnXcpConnect(char ecuName[])
{
   mMode = 255;
   mSegmentNr = 0;
   write("Connect callback! ECU: %s", ecuName);
   XcpGetCalPage(ecuName, mMode, mSegmentNr);
}

void OnXcpGetCalPage(char ecu[], long reserved1, long reserved2, long pageNumber)
{
   Write("OnXcpGetCalPage callback! ECU: %s. Current PageNumber: %d", ecu, pageNumber);
   if (pageNumber == 0)
   {
      pageNumber = 1;
   }
   else
   {
      pageNumber = 0;
   }
   XcpSetCalPage(ecu, mMode, mSegmentNr, pageNumber);
}

void OnXcpSetCalPage(char ecu[])
{
   Write("OnXcpSetCalPage callback! ECU: %s", ecu);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.1 | 13.0 | — | — | 1.0 |
| Restricted To | — | XCP | XCP | — | — | XCP |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
