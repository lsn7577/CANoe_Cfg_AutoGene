# _Diag_PreSend

> Category: `KLine` | Type: `function`

## Syntax

```c
_Diag_Presend(BYTE data[], WORD& dataLenInOut, WORD headerLen)
```

## Description

Is called before a frame is transmitted. Allows manipulating the frame.

## Parameters

| Name | Description |
|---|---|
| data | Transmitted data buffer of the frame. |
| dataLenInOut | Indicates the length of the frame when _Diag_PreSend is called. Determines the length of the frame before the frame is transmitted. |
| headerLen | Length of the header of a frame. Not supported yet |

## Return Values

—

## Example

```c
_Diag_Presend(BYTE data[], WORD& dataLenInOut, WORD headerLen)
{
   if (!gDoPatchInPreSend) // Global variable
   {
      return;
   }

   gDoPatchInPreSend = 0; // deactivate patching

   // Changing the data and the length of the request
   data[2] = 0x99;
   data[3] = 0x99;
   dataLenInOut = 4;
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.0 | 8.0 | — | — | — | 1.1 SP2 |
| Restricted To | K-Line Real bus mode Online mode ECU tester | K-Line Real bus mode Online mode ECU simulation ECU tester | — | — | — | K-Line Real bus mode Online mode ECU simulation ECU tester |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
