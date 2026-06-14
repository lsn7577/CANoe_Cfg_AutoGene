# vtsSetMinCurrentMeasurementRange

> Category: `VTSystem` | Type: `function`

## Syntax

```c
long vtsSetMinCurrentMeasurementRange (char target[], dword range);
```

## Description

Sets the current measurement range that should be used by the automatic measuring range changeover of the VT7001 module.Amperage ranges below the ranges set in range parameter will no longer be used. This prevents a measuring range changeover in dedicated situations.

Even if the measuring range for a specified amperage is not used, this does not mean, that no measurement is possible. Since the optimal Shunt is not used in such situations, the accuracy of the measurement decreases below the given value in the manual. The accuracy decreases all the more the more the used measuring range differs from the optimum. Therefore the range should be set advisedly.

## Return Values

0: Successful call

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
   vtsSetMinCurrentMeasurementRange( "VTS::ECUSupply", eVTSInterconnectionModeSup1A);
   TestWaitForTimeOut(50);

   // activate supply output
   @sysvar::VTS::ECUSupply::Active = 1;

   // activation can be measured without measuring range changeover
}
```

## Availability

| Since Version |
|---|
