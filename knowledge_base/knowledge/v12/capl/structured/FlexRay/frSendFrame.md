# frSendFrame

> Category: `FlexRay` | Type: `function`

## Syntax

```c
frSendFrame( <frame name>, dword flags, byte dataBytes[] );
```

## Description

This function generates a FlexRay frame and sends it on the bus. The FlexRay communication controller sends the message at the next possible point in time.The message must be registered before sending (see frSetSendFrame function).

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

| Since Version |
|---|
