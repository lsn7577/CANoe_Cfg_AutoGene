# SetThreshold

> Category: `VTSystem` | Type: `function`

## Syntax

```c
long SysVarNamespace.SetThreshold (eVTSThresholdGroup Group, double Threshold);
```

## Description

Sets the threshold value for differentiating between high and low levels of a group of channels on a VT2848 module.There is only one threshold setting for each group.Voltages at the input exceeding this threshold value are evaluated as high level and voltages undershooting it are evaluated as low level.

## Return Values

0: Successful call

## Example

The following example demonstrates how to configure the first channel of a VT2848 module for PWM measurement. The channel used in this example is called RPM_Sensor, the VT2848 is called Sensors.

```c
PWMMeasurement ()
{
   // Set the PWM thresholds of channels 1 to 8 to 2.5V
   sysvar::VTS::Sensors.SetThreshold(eVTSThresholdGroupChannels1To8, 2.5);

   // Set the PWM measurement duration of the first channel to 100ms
   sysvar::VTS::RPM_Sensor.SetPWMMeasurementDuration(0.1);

   // Wait 500ms and output the measured PWM frequency and duty cycle
   TestWaitForTimeout(500);
   write("Measured frequency %fHz and DC %f", @sysvar::VTS::RPM_Sensor::PWMFreq, @sysvar::VTS::RPM_Sensor::PWMDC);
}
private void Example3()
   {
      IVTSystem vts = VTSystem.Instance;
      // Get the VT2848 module
      IVT2848 sensors = vts.GetModule<IVT2848>("Sensors");

      // Set the PWM thresholds of channels 1 to 8 to 2.5V
      sensors.Threshold1To8.Value = 2.5;

     // Set the PWM measurement duration of the first channel to 100ms
      sensors.Channel1.PWMMeasurementDuration.Value = 0.1;

      // Wait 500ms and output the measured PWM frequency and duty cycle
      Execution.Wait(500);
      Output.WriteLine(string.Format("Measured frequency {0}Hz and DC {0}%", sensors.Channel1.PWMFreq.Value, sensors.Channel1.PWMDC.Value));
   }
<vtsystem_configure title="Initialize">
      <pwm_measurement_duration channel="VTS::RPM_Sensor">0.1</pwm_measurement_duration>
      <group_threshold channel="VTS::Sensors" group="1-8">2.5</group_threshold>
   </vtsystem_configure>
      <wait title="Wait 500ms" time="500" />
      <valuecomment>
      <description>Write measured frequency</description>
      <sysvar name="PWMFreq" namespace="VTS::RPM_Sensor" />
   </valuecomment>
   <valuecomment>
      <description>Write measured duty cycle</description>
      <sysvar name="PWMDC" namespace="VTS::RPM_Sensor" />
   </valuecomment>
```

## Availability

| Since Version |
|---|
