# ResetMinMax

> Category: `VTSystem` | Type: `method`

## Syntax

```c
long SysVarNamespace.ResetMinMax ();
```

## Description

Resets the measurement of the minimum and maximum value.

## Example

This example demonstrates how to measure the minimum and maximum voltages at a VT1004 channel. After the test is started, the old min and max values are reset. Then the input voltage is analyzed for 5 seconds. After that the new min and max voltages are output to CANoe's Write Window / the test report.

```c
PerformMinMaxMeasurement ()
{
   // Initialize and wait for 5 seconds
   sysvar::VTS::TempSensor.ResetMinMax();
   TestWaitForTimeOut(5000);

   // Print measurement results to Write Window
   write("Measured voltage minimum: %0.2fV", @sysvar::VTS::TempSensor::Min);
   write("Measured voltage maximum: %0.2fV", @sysvar::VTS::TempSensor::Max);
}
public void PerformMinMaxMeasurement()
   {
      // Get VTS interface and VT1004 channel
      IVTSystem vts = VTSystem.Instance;
      IVT1004Channel tempSensor = vts.GetChannel("TempSensor") as IVT1004Channel;

      // Initialize and wait for 5 seconds
      tempSensor.ResetMinMax();
      Vector.CANoe.Threading.Execution.Wait(5000);

      // Print measurement results to Write Window
      Vector.Tools.Output.WriteLine("Measured voltage minimum: " + tempSensor.Min.Value.ToString() + "V");
      Vector.Tools.Output.WriteLine("Measured voltage maximum: " + tempSensor.Max.Value.ToString() + "V");
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
