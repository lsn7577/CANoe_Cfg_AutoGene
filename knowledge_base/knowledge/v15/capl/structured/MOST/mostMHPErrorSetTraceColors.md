# mostMHPErrorSetTraceColors

> Category: `MOST` | Type: `function`

## Syntax

```c
mostMHPErrorSetTraceColors(long font, long bkgnd);
```

## Description

Sets the text and background color for displaying the MOST event in the Trace Window. The makeRGB function can be used for the colors.

## Parameters

| Name | Description |
|---|---|
| font | Font color (RGB value) |
| bkgnd | Background color (RGB value) |

## Example

```c
OnMostMHPError (long sourceDevID, long destDevID, long fBlockID, long  instID, long functionID, long opType) 
{
   mostMHPErrorSetTraceColors(makeRGB(0, 0, 0), makeRGB(255, 0, 0)  );
   return 1; // Forward the MHPError-Event to the next node in the  Measurement Setup
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.5 | 7.5 | — | — | — | —✔ |
| Restricted To | MOST25 MOST50 MOST150 | MOST25 MOST50 MOST150 | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | — | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | — | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | —✔ |
| 32-Bit | — | — | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
