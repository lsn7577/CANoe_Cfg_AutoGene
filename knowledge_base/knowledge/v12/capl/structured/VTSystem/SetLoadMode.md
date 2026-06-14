# SetLoadMode

> Category: `VTSystem` | Type: `function`

## Syntax

```c
long SysVarNamespace.SetLoadMode (eVTSLoadMode Mode);
```

## Description

Switches the internal load to a specific mode.

## Return Values

0: Successful call

## Example

The following example demonstrates the usage of the internal load of a VT1004 channel. In this example the channel is called LowBeamLeft. The internal load is configured for resistance-control-mode with a resistance of 120 Ohm. So the electronic load functions as a constant resistor against the input.

The second part of the example shows how to use the current control mode. Here the electronic load is regulated so that a constant current flows between the two ECU lines.

```c
InternalLoad_ResistanceControl ()
{
   // Set the resistor of the internal load to 120Ohm
   @sysvar::VTS::LowBeamLeft::IntLoadResistor = 120;

   // Set internal load mode to resistance control
   sysvar::VTS::LowBeamLeft.SetLoadMode(eVTSLoadModeResistanceControl);

   // Connect ECU with internal load
   @sysvar::VTS::LowBeamLeft::RelayIntLoadA = 1;
   @sysvar::VTS::LowBeamLeft::RelayIntLoadB = 1;
}
InternalLoad_CurrentControl ()
{
   // Set the current of the internal load to 1A
   @sysvar::VTS::LowBeamLeft::IntLoadCurrent = 1;

   // Set internal load mode to current control
   sysvar::VTS::LowBeamLeft.SetLoadMode(eVTSLoadModeResistanceControl);

   // Connect ECU with internal load
   @sysvar::VTS::LowBeamLeft::RelayIntLoadA = 1;
   @sysvar::VTS::LowBeamLeft::RelayIntLoadB = 1;
}
public void InternalLoad_ResistanceControl()
   {
      // Get VTS interface and VT1004 channel
      IVTSystem vts = VTSystem.Instance;
      IVT1004Channel lowBeamLeft = vts.GetChannel("LowBeamLeft") as IVT1004Channel;

      // Set the resistor of the internal load to 120Ohm
      lowBeamLeft.IntLoadResistor.Value = 120.0;

      // Set internal load mode to resistance control
      lowBeamLeft.LoadMode.Value = LoadMode.ResistanceControl;

      // Connect ECU with internal load
      lowBeamLeft.RelayIntLoadA.Value = true;
      lowBeamLeft.RelayIntLoadB.Value = true;
   }
public void InternalLoad_CurrentControl()
   {
      // Get VTS interface and VT1004 channel
      IVTSystem vts = VTSystem.Instance;
      IVT1004Channel lowBeamLeft = vts.GetChannel("LowBeamLeft") as IVT1004Channel;

      // Set the current of the internal load to 1A
      lowBeamLeft.IntLoadCurrent.Value = 1.0;

      // Set internal load mode to current control
      lowBeamLeft.LoadMode.Value = LoadMode.CurrentControl;

      // Connect ECU with internal load
      lowBeamLeft.RelayIntLoadA.Value = true;
      lowBeamLeft.RelayIntLoadB.Value = true;
   }
<testcase title="InternalLoad_ResistanceControl" ident="">
      <set title="Set the resistor of the internal load to 120Ohm">
         <sysvar name="IntLoadResistor" namespace="VTS::LowBeamLeft">120</sysvar>
      </set>
      <vtsystem_configure title="Set internal load mode to resistor control">
         <load_mode channel="VTS::LowBeamLeft" mode="resistor" />
      </vtsystem_configure>
      <set title="Connect ECU with internal load">
         <sysvar name="RelayIntLoadA" namespace="VTS::LowBeamLeft">1</sysvar>
         <sysvar name="RelayIntLoadB" namespace="VTS::LowBeamLeft">1</sysvar>
      </set>
   </testcase>
<testcase title="InternalLoad_CurrentControl" ident="">
      <set title="Set the current of the internal load to 1A">
         <sysvar name="IntLoadCurrent" namespace="VTS::LowBeamLeft">1</sysvar>
      </set>
      <vtsystem_configure title="Set internal load mode to current control">
         <load_mode channel="VTS::LowBeamLeft" mode="current" />
      </vtsystem_configure>
      <set title="Connect ECU with internal load">
         <sysvar name="RelayIntLoadA" namespace="VTS::LowBeamLeft">1</sysvar>
         <sysvar name="RelayIntLoadB" namespace="VTS::LowBeamLeft">1</sysvar>
      </set>
   </testcase>
```

## Availability

| Since Version |
|---|
