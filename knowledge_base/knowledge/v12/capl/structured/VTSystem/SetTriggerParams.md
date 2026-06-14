# SetTriggerParams

> Category: `VTSystem` | Type: `function`

## Syntax

```c
long SysVarNamespace.SetTriggerParams (eVTSTrigger Trigger, eVTSTriggerSourceChannel SourceChannel, eVTSTriggerEdgeType EdgeType);
```

## Description

The function configures basic parameters for triggers. Further parameters can be set with the function SetTriggerParamsEx.

You can find additional information about VT System triggers on the page Triggers.

## Return Values

0: Successful call

## Example

The following example shows how triggers can be used to measure the width of a pulse that is the distance between the rising and falling edge of a pulse.

Sample Code CAPL test module

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
   edgeType = eVTSTriggerEdgeTypeRising; // rising edge
   preTriggers = 0; // no other trigger as precondition
   minPulseWidth = 0.002; // pulse must have a width of at at least 2ms

   sysvar::VTS::IgnitionChannels.SetTriggerParams( trigger, sourceChannel, edgeType);
   sysvar::VTS::IgnitionChannels.SetTriggerParamsEx( trigger, minPulseWidth, 0.0, preTriggers, 0, 0, eVTSTriggerTypeEdge);

   trigger = eVTSTrigger2;
   sourceChannel = eVTSTriggerSourceChannel1;
   edgeType = eVTSTriggerEdgeTypeFalling; // falling edge
   preTriggers = 1; // first bit set: trigger 1 must be activated as a precondition

   sysvar::VTS::IgnitionChannels.SetTriggerParams( trigger, sourceChannel, edgeType);
   sysvar::VTS::IgnitionChannels.SetTriggerParamsEx( trigger, 0.0, 0.0, preTriggers, 0, 0, eVTSTriggerTypeEdge);

   TestWaitForTimeout( 50); // wait some time to make sure the settings are transferred

   // start triggers
   trigger = eVTSTrigger1;
   sysvar::VTS::IgnitionChannels.StartTrigger( trigger);
   trigger = eVTSTrigger2;
   sysvar::VTS::IgnitionChannels.StartTrigger( trigger);

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

| Since Version |
|---|
