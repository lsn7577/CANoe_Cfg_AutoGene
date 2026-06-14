# traceSetEventColors

> Category: `Other` | Type: `function`

## Syntax

```c
long traceSetEventColors(message msg, dword font, dword bkgnd); // form 1
long traceSetEventColors(errorFrame msg, dword font, dword bkgnd) // form 2
long traceSetEventColors(pg msg, dword font, dword bkgnd) // form 3
long traceSetEventColors(linFrame msg, dword font, dword bkgnd) // form 4
long traceSetEventColors(mostRawMessage msg, dword font, dword bkgnd) // form 5
long traceSetEventColors(mostMessage msg, dword font, dword bkgnd) // form 6
long traceSetEventColors(mostAmsMessage msg, dword font, dword bkgnd) // form 7
long traceSetEventColors(frFrame msg, dword font, dword bkgnd) // form 8
long traceSetEventColors(frError msg, dword font, dword bkgnd) // form 9
long traceSetEventColors(FrFrameError msg, dword font, dword bkgnd) // form 10
long traceSetEventColors(FrNullFrame msg, dword font, dword bkgnd) // form 11
long traceSetEventColors(FrPDU msg, dword font, dword bkgnd) // form 12
long traceSetEventColors(FrPOCState msg, dword font, dword bkgnd) // form 13
long traceSetEventColors(FrSlot msg, dword font, dword bkgnd) // form 14
long traceSetEventColors(FrStartCycle msg, dword font, dword bkgnd) // form 15
long traceSetEventColors(FrSymbol msg, dword font, dword bkgnd) // form 16
```

## Description

Sets the text and background color for displaying msg in the Trace Window. The makeRGB function can be used for the colors.

## Parameters

| Name | Description |
|---|---|
| msg | Variable type: message, errorFrame, pg, linFrame, mostRawMessage, mostMessage, mostAmsMessage, frFrame, frError, frameError, nullFrame, pdu, pocState, slot, symbol, startCycle |
| font | Font color (RGB value) |
| bkgnd | Background color (RGB value) |

## Example

```c
on message *
{
   traceSetEventColors(this, makeRGB(0x00, 0xFF, 0xFF), makeRGB(0x00, 0x00, 0x00));
   output(this);
}
on message *
{
   message * msg;
   msg = this;
   traceSetEventColors(msg, makeRGB(0x00, 0xFF, 0xFF), makeRGB(0x00, 0x00, 0x00));
   output(msg);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.0 | 7.0 | 13.0 | — | — | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | — | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
