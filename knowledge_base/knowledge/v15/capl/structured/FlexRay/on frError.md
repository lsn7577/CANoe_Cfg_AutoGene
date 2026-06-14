# on frError

> Category: `FlexRay` | Type: `event`

## Description

The event procedure is called in the event of a general error being detected on the FlexRay bus.

## Example

The following program reacts on bus errors and prints them in the Write Window, Trace Window, and logging.

```c
variables
{
   const int cWriteTextSize = 512;
   char writeTxt[cWriteTextSize];
   const int cWriteTextSize2 = 40;
   char writeTxt2[cWriteTextSize2];
   const int writeSink_Trace           = 
 -3;
   const int writeSink_Logging         = 
 -2;
   const int writeSeverity_Information = 1;
}
on frError
{
   getFRErrorName(this.FR_Code, 
 cWriteTextSize2, writeTxt2);
   snprintf(writeTxt, cWriteTextSize, "%10.6f: on FRError %3d (%-32s) on channel %2d with HW Type %2d, Data0 0x%02x, Data1 0x%02x, Data2 0x%02x, Data3 0x%02x, Data4 0x%02x.", getTime(0), this.FR_Code, writeTxt2, (int)this.MsgChannel, this.FR_HWTag, this.FR_Data0, this.FR_Data1, this.FR_Data2, this.FR_Data3, this.FR_Data4);
   myprint(writeTxt);
   output(this); // only required in Measurement Setup
}
float getTime (float time)
{
   return TimeNowNS() / 1000000000.0;
}
void myprint(char text[])
{
   write("%s", text);
   writeLineEx(writeSink_Trace, writeSeverity_Information, "%s", text);
   writeLineEx(writeSink_Logging, writeSeverity_Information, "%s", text);
}
int getFRErrorName (word code, word nameSize, char name[])
{
   int r = -1;
   if (code == 0) {
      snprintf(name, nameSize, "No Error");
r = code;
   } else if (code == 1) {
      snprintf(name, nameSize, "FlexCard Overflow");
r = code;
   } else if (code == 2) {
      snprintf(name, nameSize, "POC Error Mode Change");
r = code;
   } else if (code == 3) {
      snprintf(name, nameSize, "Sync Frames Below Minimum");
r = code;
   } else if (code == 4) {
      snprintf(name, nameSize, "Sync Frame Overflow");
r = code;
   } else if (code == 5) {
      snprintf(name, nameSize, "Clock Correction Failure");
r = code;
   } else if (code == 6) {
      snprintf(name, nameSize, "Parity Error");
r = code;
   } else if (code == 7) {
      snprintf(name, nameSize, "Receive FIFO Overrun");
r = code;
   } else if (code == 8) {
      snprintf(name, nameSize, "Empty FIFO Access");
r = code;
   } else if (code == 9) {
    snprintf(name, 
 nameSize, "Illegal Input Buffer Access");
r = code;
   } else if (code == 10) {
      snprintf(name, nameSize, "Illegal Output Buffer Access");
r = code;
   } else if (code == 11) {
      snprintf(name, nameSize, "Syntax Error");
r = code;
   } else if (code == 12) {
     snprintf(name, nameSize, "Content Error");
r = code;
   }  else if (code == 13) {
    snprintf(name, nameSize, "Slot Boundary Violation");
r = code;
   } else if (code == 14) {
      snprintf(name, nameSize, "Transmission Across Boundary A");
r = code;
   } else if (code == 15) {
      snprintf(name, nameSize, "Transmission Across Boundary B");
r = code;
   } else if (code == 16) {
      snprintf(name, nameSize, "Latest Transmit Violation A");
r = code;
   } else if (code == 17) {
      snprintf(name, nameSize, "Latest Transmit Violation B");
r = code;
   } else if (code == 18) {
      snprintf(name, nameSize, "Error Detection on A");
r = code;
   } else if (code == 19) {
      snprintf(name, nameSize, "Error Detection on B");
r = code;
   } else if (code == 20) {
      snprintf(name, nameSize, "Message Handler Constraints Flag Error");
r = code;
   } else if (code == 21) {
      snprintf(name, nameSize, "NIT SENA");
r = code;
   } else if (code == 22) {
      snprintf(name, nameSize, "NIT SBNA");
r = code;
   } else if (code == 23) {
      snprintf(name, nameSize, "NIT SENB");
r = code;
   } else if (code == 24) {
      snprintf(name, nameSize, "NIT SBNB");
r = code;
   } else if (code == 25) {
      snprintf(name, nameSize, "Internal Error Overflow");
r = code;
   } else if (code == 26) {
      snprintf(name, nameSize, "Wrong Frame");
r = code;
   } else if (code == 27) {
      snprintf(name, nameSize, "Bus Guardian Error");
r = code;
   } else if (code == 28) {
      snprintf(name, nameSize, "CHI Error");
r = code;
   } else if (code == 29) {
      snprintf(name, nameSize, "Error Handling Level Changed");
r = code;
   } else if (code == 30) {
      snprintf(name, nameSize, "Symbol Received");
r = code;
   } else {
      snprintf(name, nameSize, "Unknown");
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

| Time (data type dword) | The error time stamp that has been synchronized with the global time base in the computer (CAN hardware or computer system clock). The time stamp must be used if time relations should be regarded with events from other sources. This time stamp is also output in the Trace Window when receiving a symbol. Unit:10 microseconds Write-protected! |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| msgChannel | Channel in the tool that the FlexRay CC determines. Write-protected! |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| FR_HWTag | Identifies the type of the FlexRay hardware (data type: dword): 0 HW independent 1 Invalid 2 Not used 3 Not used 4 FlexCard Cyclone II 5 Vector FlexRay hardware Write-protected! | 0 | HW independent | 1 | Invalid | 2 | Not used | 3 | Not used | 4 | FlexCard Cyclone II | 5 | Vector FlexRay hardware |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0 | HW independent |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 1 | Invalid |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 2 | Not used |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 3 | Not used |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 4 | FlexCard Cyclone II |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 5 | Vector FlexRay hardware |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| FR_Code | Identifies the error type (data type: LONG) -1 Unknown error 0 NO error 1 FlexCard Overflow 2 POC Error Mode Changed 3 Sync Frames Below Minimum 4 Sync Frame Overflow 5 Clock Correction Failure 6 Parity Error 7 Receive FIFO Overrun 8 Empty FIFO Access 9 Illegal Input Buffer Access 10 Illegal Output Buffer Access 11 Syntax Error 12 Content Error 13 Slot Boundary Violation 14 Transmission Across Boundary Channel A 15 Transmission Across Boundary Channel B 16 Latest Transmit Violation Channel A 17 Latest Transmit Violation Channel B 18 Error Detection on Channel A 19 Error Detection on Channel B 20 Message Handler Constraints Flag Error 21 NIT SENA (Syntax Error during NIT Channel A) 22 NIT SBNA (Slot Boundary Violation during NIT Channel A) 23 NIT SENB (Syntax Error during NIT Channel B) 24 NIT SBNB (Slot Boundary Violation during NIT Channel B) 25 Internal Error Overflow 26 Wrong Frame 27 Bus Guardian Error 28 CHI Error 29 Error Handling Level Changed 30 Symbol Received Write-protected! | -1 | Unknown error | 0 | NO error | 1 | FlexCard Overflow | 2 | POC Error Mode Changed | 3 | Sync Frames Below Minimum | 4 | Sync Frame Overflow | 5 | Clock Correction Failure | 6 | Parity Error | 7 | Receive FIFO Overrun | 8 | Empty FIFO Access | 9 | Illegal Input Buffer Access | 10 | Illegal Output Buffer Access | 11 | Syntax Error | 12 | Content Error | 13 | Slot Boundary Violation | 14 | Transmission Across Boundary Channel A | 15 | Transmission Across Boundary Channel B | 16 | Latest Transmit Violation Channel A | 17 | Latest Transmit Violation Channel B | 18 | Error Detection on Channel A | 19 | Error Detection on Channel B | 20 | Message Handler Constraints Flag Error | 21 | NIT SENA (Syntax Error during NIT Channel A) | 22 | NIT SBNA (Slot Boundary Violation during NIT Channel A) | 23 | NIT SENB (Syntax Error during NIT Channel B) | 24 | NIT SBNB (Slot Boundary Violation during NIT Channel B) | 25 | Internal Error Overflow | 26 | Wrong Frame | 27 | Bus Guardian Error | 28 | CHI Error | 29 | Error Handling Level Changed | 30 | Symbol Received |
| -1 | Unknown error |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0 | NO error |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 1 | FlexCard Overflow |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 2 | POC Error Mode Changed |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 3 | Sync Frames Below Minimum |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 4 | Sync Frame Overflow |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 5 | Clock Correction Failure |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 6 | Parity Error |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 7 | Receive FIFO Overrun |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 8 | Empty FIFO Access |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 9 | Illegal Input Buffer Access |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 10 | Illegal Output Buffer Access |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 11 | Syntax Error |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 12 | Content Error |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 13 | Slot Boundary Violation |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 14 | Transmission Across Boundary Channel A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 15 | Transmission Across Boundary Channel B |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 16 | Latest Transmit Violation Channel A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 17 | Latest Transmit Violation Channel B |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 18 | Error Detection on Channel A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 19 | Error Detection on Channel B |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 20 | Message Handler Constraints Flag Error |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 21 | NIT SENA (Syntax Error during NIT Channel A) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 22 | NIT SBNA (Slot Boundary Violation during NIT Channel A) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 23 | NIT SENB (Syntax Error during NIT Channel B) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 24 | NIT SBNB (Slot Boundary Violation during NIT Channel B) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 25 | Internal Error Overflow |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 26 | Wrong Frame |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 27 | Bus Guardian Error |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 28 | CHI Error |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 29 | Error Handling Level Changed |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 30 | Symbol Received |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| FR_Data0 | Contains extended information (data type: dword): Not used. Write-protected! |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| FR_Data1 | Contains extended information (data type: dword): Not used as yet. Write-protected! |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| FR_Data2 | Contains extended information (data type: dword): Not used as yet. Write-protected! |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| FR_Data3 | Contains extended information (data type: dword): Not used as yet. Write-protected! |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| FR_Data4 | Contains extended information (data type: dword): Not used as yet. Write-protected! |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
