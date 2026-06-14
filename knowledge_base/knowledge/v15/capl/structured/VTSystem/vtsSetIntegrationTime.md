# vtsSetIntegrationTime

> Category: `VTSystem` | Type: `function`

## Syntax

```c
long vtsSetIntegrationTime (char Target[], double IntTime);
```

## Description

Mean and RMS values are calculated in a moving measurement time window.The length of the time window can be set with this function.

## Parameters

| Name | Description |
|---|---|
| Target | Name of the system variable/namespace that will be affected by this function call. |
| IntTime | Measurement time window in seconds.VT1004/VT1104: The only permissible time settings are 128 µs (= 0.000128; mean value only), 1 ms (mean value only), 10 ms, 100 ms, and 1 s.VT2516/VT7001: The permissible time settings depend on the concrete measurement values and are similar to the possible settings in the VT System configuration dialog.If an invalid value is specified, the call will fail. |

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
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.5 SP2 | 13.0 | — | — | 1.0 |
| Restricted To | — | — | VT offline | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
