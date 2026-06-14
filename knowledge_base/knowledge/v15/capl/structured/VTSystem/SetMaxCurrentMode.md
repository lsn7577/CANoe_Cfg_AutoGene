# SetMaxCurrentMode

> Category: `VTSystem` | Type: `method`

## Syntax

```c
long SysVarNamespace.SetMaxCurrentMode (dword Mode, double Factor); // form 1
long SysVarNamespace.SetMaxCurrentMode (dword Mode); // form 2
```

## Description

Sets the mode for the control voltage output to control the power supply's maximal output current.

## Parameters

| Name | Description |
|---|---|
| 0 | Max current control voltage output not active |
| 1 | Constant value, determined by the corresponding output system variable |
| Factor | Factor to determine the control voltage from the defined (using the system variable or the wave form) power supply max current value.Power Supply Max Current * Factor = Control Voltage The factor has a default value of 1.0 at measurement start. If the function is called without factor parameter the currently set factor is kept. |

## Example

In the following example the maximum current mode is activated on the power supply channel ExtSupply of a VT7001 module. The max. current output is set to 10 A. Finally the output Clamp30 of the VT7001 is activated. To set a max current of 10 A, e.g. a control voltage of 5.0 V has to be given to the power supply. Therefore a factor of 0.5 has to be used.

```c
SetMaxCurrentMode ()
{
   // Set mode to one power supply only -> external power supply 1
   sysvar::VTS::PowerSupply.SetInterconnectionMode(1);
   // Activate the maximum current mode with constant value mode
   // and a factor of 0.5
   sysvar::VTS::ExtSupply.SetMaxCurrentMode(1, 0.5);
   // Set power supply to max 10A
   @sysvar::VTS::ExtSupply::MaxCurrent = 10.0;
   // Switch output on
   @sysvar::VTS::Clamp30::Active = 1;
}
public void SetMaxCurrentMode()
   {
      // Get VTS interface, VT7001 module, internal supply and a output channel
      IVTSystem vts = VTSystem.Instance;
      IVT7001 powerSupply = vts.GetModule("PowerSupply") as IVT7001;
      IVT7001SupplyExternal extSupply = vts.GetChannel("ExtSupply") as IVT7001SupplyExternal;
      IVT7001Channel clamp30 = vts.GetChannel("Clamp30") as IVT7001Channel;

      // Set mode to one power supply only -> external power supply 1
      powerSupply.InterconnectionMode.Value = InterconnectionMode.Sup1;

      // Activate the maximum current mode with constant value mode
      // and a factor of 0.5
      extSupply.SetMaxCurrentMode(MaxCurrentMode.Constant, 0.5);

      // Set power supply to max 10A
      extSupply.MaxCurrent.Value = 10.0;

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
