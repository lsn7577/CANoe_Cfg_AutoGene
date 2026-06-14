# _KLine_ErrorInd

> Category: `KLine` | Type: `function`

## Syntax

```c
_KLine_ErrorInd(dword errType)
```

## Description

Called when a protocol error occurred.

## Parameters

| Name | Description |
|---|---|
| dword errType | Type of the received error. |

## Return Values

—

## Example

```c
_KLine_ErrorInd( dword error)
{
   const cKLineErrorOffset = 100;
   char cKLineErrorText[18][76] =
   {
   "The connection is closed, thus no data processing possible",
   "Tx confirmation not received, i.e. the message was not sent in time",
   "Inter byte time (P1Min) violation from Ecu",
   "Inter byte time (P1Max) violation from Ecu",
   "P2Min time violation caused with an early Ecu response",
   "P2Max time violation caused with a late Ecu response",
   "P3Min time violation caused with an early tester request",
   "P3Max time violation caused with a late tester request",
   "Inter byte time (P4Min) violation from tester, so the processing is aborted",
   "Inter byte time (P4Max) violation from tester, so the processing is aborted",
   "Unexpected byte received, so the processing is aborted",
   "Invalid header format",
   "Wrong checksum received",
   "Frame length not matching with the header",
   "K-Line message with 0 data length",
   "Only Tx and Rx directions are supported",
   "Data was manipulated by PreSend and may not be K-Line conform",
   // Sentinel - print when no other text matches
   "(no additional information)"
   };
   long textIndex;
   textIndex = error - cKLineErrorOffset;
   if( textIndex <0 || textIndex >= elcount( cKLineErrorText))
   textIndex = elcount( cKLineErrorText) - 1;
   write("ErrorInd(%d) - %s", error, cKLineErrorText[textIndex]);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0 SP4 | — | — | — | 1.1 SP2 |
| Restricted To | — | K-Line Real bus mode Online mode ECU simulation | — | — | — | K-Line Real bus mode Online mode ECU simulation |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
