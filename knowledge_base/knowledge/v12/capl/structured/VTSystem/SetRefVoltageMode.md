# SetRefVoltageMode

> Category: `VTSystem` | Type: `function`

## Syntax

```c
long SysVarNamespace.SetRefVoltageMode (eVTSRefVoltageMode Mode); // form 1
```

## Description

Sets the mode for the reference voltage output to control the power supply's output voltage.

## Return Values

0: Successful call

## Example

In order to output a control voltage (VControl) which leads to the desired output voltage VOut, the VT7001 must know the power supply factor.

In the following example, the factor of the external power supply is 0.1 and the desired output voltage VOut is 15 V.

To achieve the desired output voltage (VOut), the VT7001 calculates and sets the control voltage (VControl) automatically (1.5 V =15 * 0.1), which results in an output voltage of 15 V.

```c
SetRefVoltageMode ()
{
   // Set mode to one power supply only -> external power supply 1
   sysvar::VTS::PowerSupply.SetInterconnectionMode(eVTSInterconnectionModeSup1);

   // The factor 0.1 of the external power supply is transmitted to the VT7001
   sysvar::VTS::ExtSupply.SetRefVoltageMode(eVTSRefVoltageModeConstant, 0.1);

   // The following line sets the output voltage to 15 V,
   // VControl (1.5 V) is calculated with the given factor automatically
   @sysvar::VTS::ExtSupply::RefVoltage = 15;

   // Switch output on
   @sysvar::VTS::Clamp30::Active = eVTSOutputModeActive;
}
public void SetRefVoltageMode()
   {
   // Get VTS interface, VT7001 module, internal supply and a output channel
   IVTSystem vts = VTSystem.Instance;
   IVT7001 powerSupply = vts.GetModule("PowerSupply") as IVT7001;
   IVT7001SupplyExternal extSupply = vts.GetChannel("ExtSupply") as IVT7001SupplyExternal;
   IVT7001Channel clamp30 = vts.GetChannel("Clamp30") as IVT7001Channel;

   // Set mode to one power supply only -> external power supply 1
   powerSupply.InterconnectionMode.Value = InterconnectionMode.Sup1;

   // Activate the reference voltage mode with constant value mode
   // and a factor of 0.1
   extSupply.SetRefVoltageMode(RefVoltageMode.Constant, 0.1);

   // The following line sets the output voltage to 15 V,
   // VControl (1.5 V) is calculated with the given factor automatically
   extSupply.RefVoltage.Value = 15.0;

   // Switch output on
   clamp30.Active.Value = OutputMode.Active;
   }
<testcase title="RefVoltageMode" ident="">
      <vtsystem_configure title="Initialize">
         <ref_voltage_mode channel="VTS::ExtSupply" mode="static" factor="0.1" />
         <interconnection_mode channel="VTS::PowerSupply" mode="sup1" />
      </vtsystem_configure>
      <set title="Set reference voltage">
         <sysvar name="MaxCurrent" namespace="VTS::ExtSupply">15</sysvar>
      </set>
      <set title="Activate output">
         <sysvar name="Active" namespace="VTS::Clamp30">1</sysvar>
      </set>
   </testcase>
```

## Availability

| Since Version |
|---|
