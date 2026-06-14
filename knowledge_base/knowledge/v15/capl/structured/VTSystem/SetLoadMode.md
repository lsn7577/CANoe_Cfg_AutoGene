# SetLoadMode

> Category: `VTSystem` | Type: `method`

## Syntax

```c
long SysVarNamespace.SetLoadMode (eVTSLoadMode Mode);
```

## Description

Switches the internal load to a specific mode.

## Parameters

| Name | Description |
|---|---|
| Mode | Values see eVTSLoadMode |

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
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.0 SP5 | 13.0 | — | — | 1.0 |
| Restricted To | — | — | VT offline | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
