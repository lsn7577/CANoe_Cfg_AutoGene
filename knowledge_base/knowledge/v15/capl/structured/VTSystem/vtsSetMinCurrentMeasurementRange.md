# vtsSetMinCurrentMeasurementRange

> Category: `VTSystem` | Type: `function`

## Syntax

```c
long vtsSetMinCurrentMeasurementRange (char target[], dword range); //VT7001
long vtsSetMinCurrentMeasurementRange (char target[], VTS2808CurrentMeasurementRange range); //VT2808
```

## Description

Sets the current measurement range that should be used by the automatic measuring range changeover of the VT7001/VT2808 module.Amperage ranges below the ranges set in range parameter will no longer be used. This prevents a measuring range changeover in dedicated situations.

Even if the measuring range for a specified amperage is not used, this does not mean, that no measurement is possible. Since the optimal Shunt is not used in such situations, the accuracy of the measurement decreases below the given value in the manual. The accuracy decreases all the more the more the used measuring range differs from the optimum. Therefore the range should be set advisedly.

## Parameters

| Name | Description |
|---|---|
| Target | Name of the system variable/namespace that will be affected by this function call. |
| Range | Determines up to which range the automatic measuring range changeover may changes over. Ranges for VT7001 module: Values see eVTSCurrentMeasurementRange Ranges for VT2808 module: Values see eVTS2808CurrentMeasurementRange |

## Example

This example shows how the measuring ranges up to 100mA are locked for a measurement before a load will be switched on:

```c
PerformMeasurementAtActivation()
{
   // Prepare VT7001 module (External power supply with fixed voltage is
   // connected to PS1 connector)
   vtsSetInterconnectionMode( "VTS::ECUSupplyModule", eVTSInterconnectionModeSup1);

   // Configure output to use current measurement ranges for more than 100mA
   // and wait for setting to be applied. A current below 1A is expected at
   // activation so no measuring range changeover should take place.
   vtsSetMinCurrentMeasurementRange( "VTS::ECUSupply", eVTSCurrentMeasurementRange1A);
   TestWaitForTimeOut(50);

   // activate supply output
   @sysvar::VTS::ECUSupply::Active = 1;

   // activation can be measured without measuring range changeover
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0: VT7001 12.0 SP3: VT2808 | 13.0 | — | — | 1.0: VT7001: form 1 4.0 SP3: VT2808: form 1 |
| Restricted To | — | — | VT offline | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
