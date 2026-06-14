# on frPOCState

> Category: `FlexRay` | Type: `event`

## Syntax

```c
on frPOCState
```

## Description

The event procedure is called whenever there is a change of state on the FlexRay Communication Controller's protocol operation state machine.

## Example

The following program reacts on Protocol Operation Control state changes in the FlexRay interface and prints them in the Write Window, Trace Window, and logging.

```c
variables
{
   const int cWriteTextSize = 512;
   char writeTxt[cWriteTextSize];
   const int cWriteTextSize2 = 40;
   char writeTxt2[cWriteTextSize2];
   const int writeSink_Trace           = -3;
   const int writeSink_Logging         = -2;
   const int writeSeverity_Information = 1;
   int gClusterIsAsync = -1;
}

on frPocState
{
   getPOCStateName(this.FR_POCState, cWriteTextSize2, writeTxt2);
   snprintf(writeTxt, cWriteTextSize, "%10.6f: on FRPOCState %2d (%-32s) in cycle %3d on channel %2d with HW Type %2d, Info1 0x%02x, Info2 0x%02x, Info3 0x%02x, Info4 0x%02x.", getTime(0), this.FR_POCState, writeTxt2, this.FR_Cycle, (int)this.MsgChannel, this.Type, this.FR_Info1, this.FR_Info2, this.FR_Info3, this.FR_Info4);
   myprint(writeTxt);
   output(this); // only required in Measurement Setup
   if ((this.FR_POCState != -1) && (this.FR_POCState < 100)) {
     if (((gClusterIsAsync == -1) || (gClusterIsAsync == 0)) && ((this.FR_POCState == 4) || (this.FR_POCState == -2))) {
        gClusterIsAsync = 1;
        write("gClusterIsAsync = 1");
     }
     if (((gClusterIsAsync == -1) || (gClusterIsAsync == 1)) && (this.FR_POCState == 2)) {
        gClusterIsAsync = 0;
        write("gClusterIsAsync = 0");
     }
   }
}

float getTime (float time)
{
   return TimeNowNS() / 1000000000.0;
}

void myprint(char text[])
{
   write("%s", text);
   writeLineEx(writeSink_Trace,   writeSeverity_Information, "%s", text);
   writeLineEx(writeSink_Logging, writeSeverity_Information, "%s", text);
}

int getPOCStateName (int state, word nameSize, char name[])
{
   int r = -1;
   if (state == -2) {
      snprintf(name, nameSize, "Synchronization Lost");
      r = state;
   } else if (state == 0x00) {
      snprintf(name, nameSize, "Default Config");
      r = state;
   } else if (state == 0x01) { 
      snprintf(name, nameSize, "Ready");
      r = state;
   } else if (state == 0x02) { 
      snprintf(name, nameSize, "Normal Active");
      r = state;
   } else if (state == 0x03) { 
      snprintf(name, nameSize, "Normal Passive");
      r = state;
   } else if (state == 0x04) { 
      snprintf(name, nameSize, "Halt");
      r = state;
   } else if (state == 0x05) { 
      snprintf(name, nameSize, "Monitor Mode");
      r = state;
   } else if (state == 0x0f) { 
      snprintf(name, nameSize, "Config");
      r = state;
   } else if (state == 0x10) { 
      snprintf(name, nameSize, "Wakeup Standby");
      r = state;
   } else if (state == 0x11) { 
      snprintf(name, nameSize, "Wakeup Listen");
      r = state;
   } else if (state == 0x12) { 
      snprintf(name, nameSize, "Wakeup Send");
      r = state;
   } else if (state == 0x13) { 
      snprintf(name, nameSize, "Wakeup Detect");
      r = state;
   } else if (state == 0x20) { 
      snprintf(name, nameSize, "Startup Prepare");
      r = state;
   } else if (state == 0x21) { 
      snprintf(name, nameSize, "Coldstart Listen");
      r = state;
   } else if (state == 0x22) { 
      snprintf(name, nameSize, "Coldstart Collision Resolution");
      r = state;
   } else if (state == 0x23) { 
      snprintf(name, nameSize, "Coldstart Consistency Check");
      r = state;
   } else if (state == 0x24) { 
      snprintf(name, nameSize, "Coldstart Gap");
      r = state;
   } else if (state == 0x25) { 
      snprintf(name, nameSize, "Coldstart Join");
      r = state;
   } else if (state == 0x26) { 
      snprintf(name, nameSize, "Integration Coldstart Check");
      r = state;
   } else if (state == 0x27) { 
      snprintf(name, nameSize, "Integration Listen");
      r = state;
   } else if (state == 0x28) { 
      snprintf(name, nameSize, "Integration Consistency Check");
      r = state;
   } else if (state == 0x29) { 
      snprintf(name, nameSize, "Initialize Schedule");
      r = state;
   } else if (state == 0x2a) { 
      snprintf(name, nameSize, "Abort Startup");
      r = state;
   } else if (state == 0x2b) { 
      snprintf(name, nameSize, "Startup Success");
      r = state;
   } else { 
      snprintf(name, nameSize, "Unknown");
      r = -1;
   }
   return r;
}
```

## Availability

| Since Version |
|---|
