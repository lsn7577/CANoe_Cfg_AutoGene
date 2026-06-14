# frSendFrame

> Category: `FlexRay` | Type: `function`

## Syntax

```c
frSendFrame( <frame name>, dword flags, byte dataBytes[] ); // form 1
frSendFrame( int slotId, int channelMask, int len, int cycleStart, int cycleRepetition, dword flags, byte dataBytes[], int channel ); // form 2
```

## Description

This function generates a FlexRay frame and sends it on the bus. The FlexRay communication controller sends the message at the next possible point in time.

The message must be registered before sending (see frSetSendFrame function).

## Parameters

| Name | Description |
|---|---|
| slotId | Identifier of the time slot in which the message should be sent. |
| 1 | Channel A |
| 2 | Channel B |
| 3 | Channel A+B (should correspond to the registered value; see frSetSendFrame function) |
| len | Number of data bytes (maximum 254 bytes). |
| cycleStart | This number designates the base cycle. This value must be smaller than the repetition factor and lies in the range between 0 and 63.This value, together with the repetition factor, determines the "Cycle Multiplexing" of the frame. The slot ID, channel mask, and cycle multiplexing uniquely identify the message in a FIBEX database. |
| cycleRepetition | This number designates the cycle repetition factor. The value must be between 1 and 64 and must be a power of 2 (e.g. 1, 2, 4, 8, 16, 32 or 64).This value, together with the base cycle, determines the "Cycle Multiplexing" of the frame. The slot ID and the cycle multiplexing (and the cluster allocation of the FlexRay bus) uniquely identify the message in a FIBEX database. |
| Bit Mask | Meaning |
| 0x10 | Sets the send mode to event triggered (if bit not set then time-triggered mode). |
| 0x20 | Sets the payload preamble bit (with static frames, the initial databytes then contain the local NM vector; with dynamic frames, the first two bytes then designate the expanded message ID). |
| 0x80 | Tx OFF The frame is no longer sent, the corresponding slots remain empty. The flag can only be used with VN interfaces. |
| 0x200 | Disable use of In-Cycle-Repetition Flag has only effect on In-Cycle-Repetition frames. Is the flag set (1), then the frame can be sent in the slot given by the parameter slotID. Is the flag not set (0 = default), then the frame will be sent in the next slot of any of the slots that are given by the In-Cycle-Repetition definition in the database. CANoe Version ≥ 7.1 SP3 |
| 0x400 | Sets the Null Frame indicator in the header. The flag can only be used with VN interfaces. |
| databytes | Array of data bytes (payload) |
| channel | Channel number (or cluster number) |

## Return Values

—

## Example

```c
variables
{
        // Bit mask meaning in flags:
        // bit | mask | for
        //----------------------------------------------------------------
        // 0   | 1 | sync flag (1 == set)
        // 1   | 2 | startup flag (1 == set)
        // 4   | 16 | TT flag (1 == event-triggered, 0 = time-triggered)
        //
   BYTE gSta1Id      = 9;  // slot ID for frame to send
   BYTE gSta1Flags   = 16; // event-triggered
   BYTE gSta1Dlc     = 4;  // bytes
   BYTE gSta1Chan    = 3;  // send on channel A+B
   BYTE gSta1Base    = 0;  // base cycle
   BYTE gSta1Rep     = 1;  // cycle repetition
   BYTE gSta1Channel = %CHANNEL%;  // FR interface
   const long gPeriodSine     = 8000;
   const long gPeriodRect     = 1000;
   const long gAmplitudeSine  = 1000;
   const int cMaxFRBufSize = 254;
  BYTE gSta1Msg[cMaxFRBufSize]; // message buffer
}
on preStart
{
   int i;
   // Declare Tx buffer in interface:
   frSetSendFrame(gSta1Id /*frameId*/, gSta1Chan /*channelMask*/, gSta1Dlc /*len*/, gSta1Base /*cycleStart*/, gSta1Rep /*cycleRepetition*/, gSta1Flags /*flags*/, gSta1Channel /*cluster*/);
   // Initialize payload:
   for(i=0; i<gSta1Dlc; ++i)
   {
      gSta1Msg[i] = i;
   }
}
on FRStartCycle *
{
   if (this.FR_Cycle % gSta1Rep == gSta1Base)
   {
      doCalc();
      FRSend();
   }
}
FRSend ()
{
   frSendFrame(gSta1Id /*frameId*/, gSta1Chan /*channelMask*/, gSta1Dlc /*len*/, gSta1Base /*cycleStart*/, gSta1Rep /*cycleRepetition*/, gSta1Flags /*flags*/, gSta1Msg /*dataBytes*/, gSta1Channel /*cluster*/);
}
doCalc ()
{
   float sine
   BYTE  rect;
   long sinel;
   // Calculating sine wave and rectangle values:
   sine = gAmplitudeSine*sin((timeNow()/100)*2*PI/gPeriodSine);
   if (sin((timeNow()/100)*2*PI/gPeriodRect)<0)
      rect = 0;
   else 
      rect = 1;
   sinel = sine;
   // assigning values to message buffer:
   gSta1Msg[0] = (sinel & 0x000000FF);
   gSta1Msg[1] = (sinel & 0x0000FF00) >> 8;
   gSta1Msg[2] = rect;
   gSta1Msg[3] = 0;
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.2 | 5.2 | 13.0 | — | — | 1.0 |
| Restricted To | FlexRay | FlexRay | FlexRay | — | — | FlexRay |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
