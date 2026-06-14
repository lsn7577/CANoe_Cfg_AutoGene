# on frSymbol

> Category: `FlexRay` | Type: `event`

## Description

The event procedure is called whenever a symbol (wake-up, CAS, MTS) is received.

## Example

The following program reacts on received symbols and prints them in the Write Window, Trace Window, and logging.

```c
variables
{
   const 
 int cWriteTextSize = 512;
   char 
 writeTxt[cWriteTextSize];
   const int cWriteTextSize2 = 40;
   char writeTxt2[cWriteTextSize2];
   const int writeSink_Trace           = 
 -3;
   const int writeSink_Logging         = 
 -2;
   const int writeSeverity_Information = 1;
}
on frSymbol
{
   getFRSymbolName(this.FR_Symbol, 
 cWriteTextSize2, writeTxt2);
   snprintf(writeTxt, cWriteTextSize, "%10.6f: on FRSymbol   %2d 
 (%-32s) in cycle %3d on channel %2d with Mask %d, Length %d.", getTime(0), this.FR_Symbol, writeTxt2, this.FR_Cycle, (int)this.MsgChannel, this.FR_ChannelMask, this.FR_Length);
   myprint(writeTxt);
   output(this); 
 // only required in Measurement Setup
}
float getTime (float time)
{
   return TimeNowNS() / 1000000000.0;
}
void myprint(char text[])
{
   write("%s", 
 text);
   writeLineEx(writeSink_Trace,   writeSeverity_Information, "%s", text);
   writeLineEx(writeSink_Logging, 
 writeSeverity_Information, "%s", text);
}
int getFRSymbolName (word symbol, word nameSize, char name[])
{
  int r = -1;
  if (symbol == 0) {
      snprintf(name, nameSize, "Unknown");
r = symbol;
  } 
 else if (symbol == 1) { 
      snprintf(name, 
 nameSize, "CAS");
r = symbol;
   } else if (symbol == 2) { 
      snprintf(name, 
 nameSize, "MTS");
r = symbol;
  } 
 else if (symbol == 3) { 
      snprintf(name, 
 nameSize, "Wakeup Symbol");
r = symbol;
   } else { 
      snprintf(name, nameSize, "Unspecified");
r = -1;
   }
   return r;
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 6.1 SP2 | 6.1 SP2 | 13.0 | — | — | 1.0 |
| Restricted To | FlexRay | FlexRay | FlexRay | — | — | FlexRay |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |

## Selectors

| Time (data type dword) | The symbol time stamp that has been synchronized with the global time base in the computer (CAN hardware or computer system clock). The time stamp must be used if time relations should be regarded with events from other sources. This time stamp is also output in the Trace Window when receiving a symbol.. Unit:10 microseconds Write-protected! |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| msgChannel | Channel in the tool that the FlexRay CC determines. Write-protected! |  |  |  |  |  |  |  |  |  |  |  |
| FR_ChannelMask | Identifies the FlexRay channel of the CC. With 1 the symbol was received on channel A, with 2 on channel B. Write-protected! |  |  |  |  |  |  |  |  |  |  |  |
| FR_Symbol | Identifies the symbol type (data type: WORD) 0 unknown 1 CAS 2 MTS 3 Wakeup 4 Undefined (used with VN interfaces in asynchronous mode) Caution! Any wake-up symbol will only be received, if the wake-up was initiated externally. Thus, if CANoe initiates a wake-up procedure, then use the handler on frPocState in order to observe the wake-up pattern transmission! Write-protected! | 0 | unknown | 1 | CAS | 2 | MTS | 3 | Wakeup | 4 | Undefined (used with VN interfaces in asynchronous mode) | Caution! Any wake-up symbol will only be received, if the wake-up was initiated externally. Thus, if CANoe initiates a wake-up procedure, then use the handler on frPocState in order to observe the wake-up pattern transmission! |
| 0 | unknown |  |  |  |  |  |  |  |  |  |  |  |
| 1 | CAS |  |  |  |  |  |  |  |  |  |  |  |
| 2 | MTS |  |  |  |  |  |  |  |  |  |  |  |
| 3 | Wakeup |  |  |  |  |  |  |  |  |  |  |  |
| 4 | Undefined (used with VN interfaces in asynchronous mode) |  |  |  |  |  |  |  |  |  |  |  |
| Caution! Any wake-up symbol will only be received, if the wake-up was initiated externally. Thus, if CANoe initiates a wake-up procedure, then use the handler on frPocState in order to observe the wake-up pattern transmission! |  |  |  |  |  |  |  |  |  |  |  |  |
| FR_Length | Indicates the length (data type: WORD) of the symbol in bit times. Write-protected! |  |  |  |  |  |  |  |  |  |  |  |
| FR_Cycle | Current FlexRay cycle number. Write-protected! |  |  |  |  |  |  |  |  |  |  |  |
| on frPocState | CAPLfunctionOnFRPocState.htm |  |  |  |  |  |  |  |  |  |  |  |
