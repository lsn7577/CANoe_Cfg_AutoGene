# on frSymbol

> Category: `FlexRay` | Type: `event`

## Syntax

```c
on frSymbol
```

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

| Since Version |
|---|
