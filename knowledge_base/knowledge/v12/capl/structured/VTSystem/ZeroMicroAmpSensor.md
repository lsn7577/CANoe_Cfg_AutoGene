# ZeroMicroAmpSensor

> Category: `VTSystem` | Type: `function`

## Syntax

```c
long SysVarNamespace.ZeroMicroAmpSensor ();
```

## Description

Zeroes the µA current sensor of a simulated battery cell of the Comemso Battery Cell Simulator.

## Return Values

0: Successful call

## Example

Micro ampere sensor is zeroed before testing charging and discharging processes.

Sample code for a single cell. Checked limits are not based on real-world battery cells!

```c
double chargingCurrent = 0.0;
double dischargingCurrent = 0.0;

// Prepare: zero micro ampere sensor while no current is going through the cell simulator
sysvar::VTS::Cell1.ZeroMicroAmpSensor();

// Set up cell simulation
@sysvar::VTS::Cell1::SettingsMode = 1;
@sysvar::VTS::Cell1::LoadSetting = 1.0;
@sysvar::VTS::Cell1::OperationMode = 1;

// initiate charging process
//...

// Check for expected charging current after on minute
testWaitForTimeout( 60000);
chargingCurrent = @sysvar::VTS::Cell1::CurrentMeasure;
if (chargingCurrent < 0.8 || chargingCurrent > 1.1)
{
  TestStepFail("Test Failure", "Unexpected charging current occurred!");
}

// initiate mode where simulated cell provides a very small current
//...

// Check for expected discharging current after 10 seconds
testWaitForTimeout( 10000);
dischargingCurrent = @sysvar::VTS::Cell1::CurrentMeasure;
if (dischargingCurrent < 0.0001 || dischargingCurrent > 0.0004)
{
  TestStepFail("Test Failure", "Unexpected charging current occurred!");
}
```

## Availability

| Since Version |
|---|
