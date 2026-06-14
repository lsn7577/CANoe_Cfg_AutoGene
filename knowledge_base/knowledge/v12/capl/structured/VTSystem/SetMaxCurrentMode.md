# SetMaxCurrentMode

> Category: `VTSystem` | Type: `function`

## Syntax

```c
long SysVarNamespace.SetMaxCurrentMode (dword Mode, double Factor);
```

## Description

Sets the mode for the control voltage output to control the power supply's maximal output current.

## Parameters

| Name | Description |
|---|---|
| 0 | Max current control voltage output not active |
| 1 | Constant value, determined by the corresponding output system variable |

## Return Values

0: Successful call

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
<testcase title="MaxCurrentMode" ident="">
      <vtsystem_configure title="Initialize">
         <max_current_mode channel="VTS::ExtSupply" mode="static" factor="0.5" />
         <interconnection_mode channel="VTS::PowerSupply" mode="sup1" />
      </vtsystem_configure>
      <set title="Set maximum current">
         <sysvar name="MaxCurrent" namespace="VTS::ExtSupply">10</sysvar>
      </set>
      <set title="Activate output">
         <sysvar name="Active" namespace="VTS::Clamp30">1</sysvar>
      </set>
   </testcase>
```

## Availability

| Since Version |
|---|
