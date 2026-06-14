# SetMeasurementMode

> Category: `VTSystem` | Type: `function`

## Syntax

```c
long SysVarNamespace.SetMeasurementMode (eVTSMeasurementMode Mode); // VT1004/VT1104
```

## Description

Controls the internal measuring instrument.

VT1004/VT1104: It is possible to switch between direct and filtered differential voltage measurement as well as measurement of pin a or b to reference ground (AGND).

VT2816: For the measurement channels (1-12) it is possible to switch between different voltage measurement modes and the current measurement mode.

## Return Values

0: Successful call

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
<testcase title="MeasurementAToAGnd" ident="">
      <vtsystem_configure title="Set measurement mode">
         <measurement_mode channel="VTS::TempSensor" mode="a_only" />
      </vtsystem_configure>
      <valuecomment>
         <description>Current sensor voltage</description>
         <sysvar name="VTS::TempSensor::Cur" />
      </valuecomment>
   </testcase>
```

## Availability

| Since Version |
|---|
