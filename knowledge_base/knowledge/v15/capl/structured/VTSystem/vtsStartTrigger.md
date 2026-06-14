# vtsStartTrigger

> Category: `VTSystem` | Type: `function`

## Syntax

```c
long SysVarNamespace.SetTriggerParams (eVTSTrigger Trigger, dword SourceChannel, dword EdgeType);
```

## Description

The function starts the specified trigger. It also resets the event counter system variable that is associated to the trigger to 0. To use a trigger it has to be configured using the functions vtsSetTriggerParams and vtsSetTriggerParamsEx.

You can find additional information about VT System triggers on the page Triggers.

## Parameters

| Name | Description |
|---|---|
| Target | Name of the system variable/namespace that will be affected by this function call. |
| Trigger | Specifies which trigger is configured.VT1004/VT1104 module: Values see eVTSTrigger |

## Example

```c
variables
{
   int64 gRiseTime = 0;
   int64 gFallTime = 0;
}

void MainTest ()
{
   MeasurePulseLength();
}

void MeasurePulseLength()
{
   dword trigger1EventCount = 0;
   dword trigger2EventCount = 0;
   int64 pulseWidth = 0;

   enum eVTSTrigger trigger = eVTSTrigger1;
   enum eVTSTriggerSourceChannel sourceChannel = eVTSTriggerSourceChannel1;
   enum eVTSTriggerEdgeType edgeType = eVTSTriggerEdgeTypeRising;
   dword preTriggers = 0;

   double minPulseWidth = 0.0;

   // configure two triggers (one for the rising and one for the falling edge)
   trigger = eVTSTrigger1;
   sourceChannel = eVTSTriggerSourceChannel1;
   edgeType = 0; // rising edge
   preTriggers = 0; // no other trigger as precondition
   minPulseWidth = 0.002; // pulse must have a width of at at least 2ms

   vtsSetTriggerParams( "VTS::IgnitionChannels", trigger, sourceChannel, edgeType);
   vtsSetTriggerParamsEx( "VTS::IgnitionChannels",  trigger, minPulseWidth, 0.0, preTriggers, 0, 0, eVTSTriggerTypeEdge);

   trigger = eVTSTrigger2;
   sourceChannel = eVTSTriggerSourceChannel1;
   edgeType = eVTSTriggerEdgeTypeFalling; // falling edge
   preTriggers = 1; // first bit set: trigger 1 must be activated as a precondition

   vtsSetTriggerParams( "VTS::IgnitionChannels",  trigger, sourceChannel, edgeType);
   vtsSetTriggerParamsEx( "VTS::IgnitionChannels",  trigger, 0.0, 0.0, preTriggers, 0, 0, eVTSTriggerTypeEdge);

   TestWaitForTimeout( 50); // wait some time to make sure the settings are transferred

   // start triggers
   trigger = eVTSTrigger1;
   vtsStartTrigger( "VTS::IgnitionChannels", trigger);
   trigger = eVTSTrigger2;
   vtsStartTrigger( "VTS::IgnitionChannels", trigger);

   // wait some time until a pulse has occurred
   TestWaitForTimeout( 1000);

   // check if pulse was detected and output pulse width
   trigger1EventCount = @sysvar::VTS::IgnitionChannels::Trigger1EventCount;
   trigger2EventCount = @sysvar::VTS::IgnitionChannels::Trigger2EventCount;

   if (trigger1EventCount > 0 && trigger2EventCount > 0)
   {
      pulseWidth = gFallTime - gRiseTime;
      Write( "Pulse width: %.3f µs", (pulseWidth/1000.0));
   }
   else
   {
      Write("No pulse detected!");
   }
}

on sysvar_update sysvar::VTS::IgnitionChannels::Trigger1Event
{
   // save time stamp of rising edge when event occurs
   gRiseTime = sysGetVariableTimeNS( this);
}

on sysvar_update sysvar::VTS::IgnitionChannels::Trigger2Event
{
   // save time stamp of falling edge when event occurs
   gFallTime = sysGetVariableTimeNS( this);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0 SP4 | 13.0 | — | — | 1.0 |
| Restricted To | — | — | VT offline | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
