# SetMeasurementMode

> Category: `VTSystem` | Type: `method`

## Syntax

```c
long SysVarNamespace.SetMeasurementMode (eVTSMeasurementMode Mode); // VT1004/VT1104
long SysVarNamespace.SetMeasurementMode (eVTS2816MeasurementMode Mode); // VT2816
```

## Description

Controls the internal measuring instrument.

VT1004/VT1104: It is possible to switch between direct and filtered differential voltage measurement as well as measurement of pin a or b to reference ground (AGND).

VT2816: For the measurement channels (1-12) it is possible to switch between different voltage measurement modes and the current measurement mode.

## Parameters

| Name | Description |
|---|---|
| Mode | Modes for VT1004/VT1104 module: Values see eVTSMeasurementMode Modes for VT2816 module: Values see eVTS2816MeasurementMode |

## Example

This example demonstrates how change the measurement mode of a VT1004 channel. By default the voltage is measured between the two input lines A and B. This example shows how to configure a measurement between input line A and the VT1004 module’s AGND.

```c
MeasurementAToAGnd ()
{
   // Change measurement mode from differential
   // to line A against ground (AGND)
   sysvar::VTS::TempSensor.SetMeasurementMode(eVTSMeasurementModeLineAToGnd);

   // Measure the voltage between line A and AGND
   write("Current voltage: %0.2fV", @sysvar::VTS::TempSensor::Cur);
}
public void MeasurementAToAGnd()
   {
      // Get VTS interface and VT1004 channel
      IVTSystem vts = VTSystem.Instance;
      IVT1004Channel tempSensor = vts.GetChannel("TempSensor") as IVT1004Channel;

      // Change measurement mode from differential
      // to line A against ground (AGND)
      tempSensor.MeasurementMode.Value = MeasurementMode.LineAToGnd;

      // Print measurement results to Write Window
      Vector.Tools.Output.WriteLine("Current voltage: " + tempSensor.Cur.Value + "V");
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
