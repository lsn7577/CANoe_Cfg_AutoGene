# vtsSetPWMMeasurementDuration

> Category: `VTSystem` | Type: `function`

## Syntax

```c
long vtsSetPWMMeasurementDuration (char Target[], double Duration);
```

## Description

During measurement of PMW Parameters with the Modules VT1004/VT1104, VT2516 or VT2848 a Duty Cicle of 0 or 100% is shown, if during the defined time no edge was recognized. This time is set with vtsSetPWMMeasurementDuration (SetPWMMeasurementDuration). Usefully, the set time should be greater than the period of the lowest frequency to be measured.So that 0% or 100% duty cycle could be identified as quickly as possible, the time should not be set to too high, because in the meantime the old values are still displayed.

## Return Values

0: Successful call

## Example

This example demonstrates how to do a PWM measurement on a channel of a VT1004 module. In this example the channel is called RPMSensor and assumed to be connected to a sensor which generates a PWM signal. Every second the measured frequency and duty cycle are written to CANoe's Write Window / once to the test report.

```c
PerformPWMMeasurement ()
{
   // Declare variables to hold measured data
   float frequency;
   float dutyCycle;

   // Configure channel for PWM measurement
   vtsSetPWMMeasurementDuration("VTS::RPMSensor", 0.1); // 100ms
   vtsSetPWMThreshold("VTS::RPMSensor", 2.5);           // 2.5V

   // Print measurement results to Write Window every second
   while(1)
   {
      // Get measured values from VT System system variables
      frequency = @sysvar::VTS::RPMSensor::PWMFreq;
      dutyCycle = @sysvar::VTS::RPMSensor::PWMDC;

      write("Frequency: %0.2fHz, Duty Cycle: %0.2f%%.", frequency, dutyCycle);
      TestWaitForTimeOut(1000);
   }
}
public void PerformPWMMeasurement()
   {
      // Get VTS interface and VT1004 channel
      IVTSystem vts = VTSystem.Instance;
      IVT1004Channel rpmSensor = vts.GetChannel("RPMSensor") as IVT1004Channel;

      // Configure channel for PWM measurement
      rpmSensor.PWMMeasurementDuration.Value = 0.1; // 100ms
      rpmSensor.PWMThreshold.Value = 2.5; // 2.5V

      // Print measurement results to Write Window every second
      while (true)
      {
         Vector.Tools.Output.WriteLine("Frequency: " + rpmSensor.PWMFreq.Value + "Hz");
         Vector.Tools.Output.WriteLine("DutyCycle: " + rpmSensor.PWMDC.Value + "%");
         Vector.CANoe.Threading.Execution.Wait(1000);
      }
   }
<testcase title="PerformPWMMeasurement" ident="">
      <vtsystem_configure title="Configure PWM measurement">
         <pwm_measurement_duration channel="VTS::RPMSensor">0.1</pwm_measurement_duration>
         <pwm_threshold channel="VTS::RPMSensor">2.5</pwm_threshold>
      </vtsystem_configure>
      <wait time="100" title="Wait 100ms" />
      <valuecomment>
         <description>RPM sensor duty cycle</description>
         <sysvar name="VTS::RPMSensor::PWMDC"></sysvar>
      </valuecomment>
      <valuecomment>
         <description>RPM sensor frequency</description>
         <sysvar name="VTS::RPMSensor::PWMFreq"></sysvar>
      </valuecomment>
   </testcase>
```

## Availability

| Since Version |
|---|
