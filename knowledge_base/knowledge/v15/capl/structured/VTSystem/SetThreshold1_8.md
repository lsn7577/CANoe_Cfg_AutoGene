# SetThreshold1_8

> Category: `VTSystem` | Type: `method`

## Syntax

```c
long SysVarNamespace.SetThreshold1_8 (double Threshold);
```

## Description

Sets the threshold value for differentiating between high and low levels of the channels 1…8 of a digital module VT2516.There is only one threshold setting for all eight channels together.Voltages at the input exceeding this threshold value are evaluated as high level and voltages undershooting it are evaluated as low level.

## Parameters

| Name | Description |
|---|---|
| Threshold | Voltage value in volts in the range from 0…25 V. |

## Example

The following example demonstrates how to measure a PWM signal on a VT2516 channel (e.g. a ECU output that controls an LED). The measured frequency and duty cycle is then output to the Write Window / the test report.

```c
PWMMeasurement ()
{
   // Declare variables to hold measured data
   float frequency;
   float dutyCycle;

   // Set threshold for channels 1-8 to 2.5 V
   sysvar::VTS::DigitalSignals.SetThreshold1_8(3.5);

   // Set maximum measurement duration to 100 ms
   // (because the lowest PWM frequency is 100 Hz)
   sysvar::VTS::LED.SetPWMMeasurementDuration(0.1);

   // Wait 100 ms and read measured PWM parameters
   TestWaitForTimeout (100);
   frequency = @sysvar::VTS::LED::PWMFreq;
   dutyCycle = @sysvar::VTS::LED::PWMDC;

   // Output measured values to the Write Window
   write("Frequency: %0.2fHz, Duty Cycle: %0.2f%%.", frequency, dutyCycle);
}
public void PWMMeasurement()
   {
      // Get VTS interface, VT2516 module and VT2516 channel
      IVTSystem vts = VTSystem.Instance;
      IVT2516 vt2516 = vts.GetModule("DigitalSignals") as IVT2516;
      IVT2516Channel led = vts.GetChannel("LED") as IVT2516Channel;

      // Set threshold for channels 1-8 to 2.5 V
      vt2516.Threshold1To8.Value = 3.5;

      // Set maximum measurement duration to 100 ms
      // (because the lowest PWM frequency is 100 Hz)
      led.PWMMeasurementDuration.Value = 0.1;

      // Wait 100 ms and read measured PWM parameters
      Vector.CANoe.Threading.Execution.Wait(100);
      double frequency = led.PWMFreq.Value;
      double dutyCycle = led.PWMDC.Value;

      // Output measured values to the Write Window
      Vector.Tools.Output.WriteLine("Frequency: " + frequency + "Hz");
      Vector.Tools.Output.WriteLine("DutyCycle: " + dutyCycle + "%");
   }
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.2 | 13.0 | — | — | 1.0 |
| Restricted To | — | — | VT offline | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
