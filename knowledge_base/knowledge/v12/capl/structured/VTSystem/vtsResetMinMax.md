# vtsResetMinMax

> Category: `VTSystem` | Type: `function`

## Syntax

```c
long vtsResetMinMax (char Target[]);
```

## Description

Resets the measurement of the minimum and maximum value.

## Return Values

0: Successful call

## Example

This example demonstrates how to measure the minimum and maximum voltages at a VT1004 channel. After the test is started, the old min and max values are reset. Then the input voltage is analyzed for 5 seconds. After that the new min and max voltages are output to CANoe's Write Window / the test report.

```c
PerformMinMaxMeasurement ()
{
   // Initialize and wait for 5 seconds
   vtsResetMinMax("VTS::TempSensor");
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
<testcase title="PerformMinMaxMeasurement" ident="">
      <vtsystem_configure title="Reset min and max values">
         <reset_min_max channel="VTS::TempSensor" />
      </vtsystem_configure>
      <wait time="5000" title="Wait 5s" />
      <valuecomment>
         <description>Minimum value that occurred during the last 5s</description>
         <sysvar name="VTS::TempSensor::Min" />
      </valuecomment>
      <valuecomment>
         <description>Maximum value that occurred during the last 5s</description>
         <sysvar name="VTS::TempSensor::Max"></sysvar>
      </valuecomment>
   </testcase>
```

## Availability

| Since Version |
|---|
