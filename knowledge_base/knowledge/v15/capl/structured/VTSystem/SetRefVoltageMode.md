# SetRefVoltageMode

> Category: `VTSystem` | Type: `method`

## Syntax

```c
long SysVarNamespace.SetRefVoltageMode (eVTSRefVoltageMode Mode); // form 1
long SysVarNamespace.SetRefVoltageMode (eVTSRefVoltageMode Mode, double Factor); // form 2
```

## Description

Sets the mode for the reference voltage output to control the power supply's output voltage.

## Parameters

| Name | Description |
|---|---|
| Mode | Values see eVTSRefVoltageMode |
| Note The factor is given by the external power supply. This factor is the ratio of the control voltage to the output voltage. For example, if a power supply outputs 50 V at a control voltage of 5 V, its factor is 0.1 (5/50). |  |

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
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.2 | 13.0 | — | — | 1.0 |
| Restricted To | — | — | VT offline | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
