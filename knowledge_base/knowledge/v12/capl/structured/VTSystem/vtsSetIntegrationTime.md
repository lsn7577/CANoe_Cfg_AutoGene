# vtsSetIntegrationTime

> Category: `VTSystem` | Type: `function`

## Syntax

```c
long vtsSetIntegrationTime (char Target[], double IntTime);
```

## Description

Mean and RMS values are calculated in a moving measurement time window.The length of the time window can be set with this function.

## Return Values

0: Successful call

## Example

This example demonstrates how to change the integration time of a VT System system variable during the measurement. The integration time is set to 1s to cancel out noise in the sensor readings. It is assumed that the sensor to be read is connected to a channel called TempSensor of the VT1004 module.

```c
SetIntegrationTime ()
{
   // Set integration time to 1 second
   vtsSetIntegrationTime("VTS::TempSensor::Avg", 1.0);

   // Output sensor readings to the Write Window every second
   while(1)
   {
      write("Average sensor value: %fV", @sysvar::VTS::TempSensor::Avg);
      TestWaitForTimeOut(1000);
   }
}
public void SetIntegrationTime()
   {
      // Get VTS interface and temperature sensor channel
      IVTSystem vts = VTSystem.Instance;
      IVT1004Channel tempSensor = vts.GetChannel("TempSensor") as IVT1004Channel;
      // Set integration time to 1 second
      tempSensor.Avg.IntegrationTime = 1.0;
      // Output sensor readings to the Write Window every second
      while (true)
      {
         Vector.Tools.Output.WriteLine("Average sensor value: " + tempSensor.Avg.Value.ToString() + "V");
         Vector.CANoe.Threading.Execution.Wait(1000);
      }
   }
<testcase title="SetIntegrationTime" ident="">
      <vtsystem_configure title="Set integration time to 1s">
         <integration_time channel="VTS::TempSensor" sysvar="Avg">1.0</integration_time>
      </vtsystem_configure>
      <wait time="1000" title="Wait 1s" />
      <valuecomment>
         <description>Average value of the sensor</description>
         <sysvar name="VTS::TempSensor::Avg"></sysvar>
      </valuecomment>
   </testcase>
```

## Availability

| Since Version |
|---|
