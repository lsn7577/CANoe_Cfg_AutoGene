# vtsSetInterconnectionMode

> Category: `VTSystem` | Type: `function`

## Syntax

```c
long vtsSetInterconnectionMode (char Target[],eVTSInterconnectionMode Mode);
```

## Description

Sets the mode for interconnection of the three possible power supplies and the two power outputs of the power module VT7001.

## Return Values

0: Successful call

## Example

The internal power supply unit delivers power and the ECU is connected to OUT1 (clamp 30), OUT2 (clamp 15) and GND1 (clamp 31). In this example, the channel for the internal power sup-ply unit is named “IntSupply”, the two output channels are named “Clamp30” and “Clamp15”, and the VT7001 module is named “PowerSupply”.

```c
InternalPowerSupply ()
{
   // Set mode to one power supply only -> internal power supply
   vtsSetInterconnectionMode("VTS::PowerSupply", eVTSInterconnectionModeSupInt);

   // Set voltage to 12.0 V
   vtsSetRefVoltageMode("VTS::IntSupply", 1);
   @sysvar::VTS::IntSupply::RefVoltage = 12.0;

   // Switch both outputs on
   @sysvar::VTS::Clamp30::Active = eVTSOutputModeActive;
   @sysvar::VTS::Clamp15::Active = eVTSOutputModeActive;

   // Measure the current consumed by the ECU via clamp 15
   // after 2 seconds (result is written to the Write Window)
   TestWaitForTimeOut(2000);
   write("ECU is consuming %fmA.", @sysvar::VTS::Clamp30::AvgCurrent);
}
public void InternalPowerSupply()
   {
      // Get VTS interface, VT7001 module, internal supply and two output channels
      IVTSystem vts = VTSystem.Instance;
      IVT7001 powerSupply = vts.GetModule("PowerSupply") as IVT7001;
      IVT7001SupplyInternal intSupply = vts.GetChannel("IntSupply") as IVT7001SupplyInternal;
      IVT7001Channel clamp30 = vts.GetChannel("Clamp30") as IVT7001Channel;
      IVT7001Channel clamp15 = vts.GetChannel("Clamp15") as IVT7001Channel;

      // Set mode to one power supply only -> external power supply 1
      powerSupply.InterconnectionMode.Value = InterconnectionMode.SupInt;

      // Set voltage to 12.0 V
      intSupply.SetRefVoltageMode(RefVoltageMode.Constant);
      intSupply.RefVoltage.Value = 12.0;

      // Switch both outputs on
      clamp30.Active.Value = OutputMode.Active;
      clamp15.Active.Value = OutputMode.Active;

      // Measure the current consumed by the ECU via clamp 15
      // after 2 seconds (result is written to the Write Window)
      Vector.CANoe.Threading.Execution.Wait(2000);
      Vector.Tools.Output.WriteLine("ECU is consuming " + clamp30.AvgCurrent.Value + "mA");
   }
<testcase title="InternalPowerSupply" ident="">
      <vtsystem_configure title="Initialize">
         <ref_voltage_mode channel="VTS::IntSupply" mode="static" />
         <interconnection_mode channel="VTS::PowerSupply" mode="supint" />
      </vtsystem_configure>
      <set title="Set voltage">
         <sysvar name="VTS::IntSupply::RefVoltage">12</sysvar>
      </set>
      <set title="Activate outputs">
         <sysvar name="VTS::Clamp15::Active">1</sysvar>
         <sysvar name="VTS::Clamp30::Active">1</sysvar>
      </set>
      <wait time="2000" title="Wait 2s" />
      <valuecomment>
         <description>Measure current going through clamp 30</description>
         <sysvar name="VTS::Clamp30::AvgCurrent"></sysvar>
      </valuecomment>
   </testcase>
```

## Availability

| Since Version |
|---|
