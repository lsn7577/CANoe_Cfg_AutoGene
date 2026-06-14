# vtsSetOutputMode

> Category: `VTSystem` | Type: `function`

## Syntax

```c
long vtsSetOutputMode (char Target[], eVTS2848OutputMode Mode);
```

## Description

Sets the mode for output on the channel.

## Return Values

0: Successful call

## Example

The following example demonstrates how to use the PWM output of a VT2848 channel to simulate a PWM based sensor (e.g. a RPM sensor). The channel used in this example is called RPM_Sensor.

```c
SimulateSensorPWM ()
{
   // The current value of the frequency (100Hz)
   float currentFrequency = 100.0;

   // Choose ′low side switch′, PWM curve type and
   // Vext as source for high value
   vtsSetOutputMode ("VTS::RPM_Sensor", eVTS2848OutputModeLowsideSwitch);
   vtsSetCurveType("VTS::RPM_Sensor", eVTSCurveTypePWM);
   vtsSetOutputSource("VTS::SensorModule1", eVTSOutputSourceGroupChannels1To4, eVTSOutputSourceVExt);

   // Set the number of repeats to unlimited
   vtsSetPWMRepeats("VTS::RPM_Sensor", 0);

   // Set initial frequency (100Hz) and duty cycle (50%) values
   @sysvar::VTS::RPM_Sensor::PWMOutputFreq = currentFrequency;
   @sysvar::VTS::RPM_Sensor::PWMOutputDC = 50.0;

   // Start the stimulation
   vtsStartStimulation("VTS::RPM_Sensor");

   // To stimulate different sensor readings increase
   // frequency of the PWM signal over time
   while(currentFrequency < 200)
   {
      // Increase the frequency by 1Hz every 100ms
      TestWaitForTimeOut(100);
      currentFrequency += 1;
      @sysvar::VTS::RPM_Sensor::PWMOutputFreq = currentFrequency;
   }

   // Stop the stimulation
   StopStimulation();
}
public void SimulateSensorPWM()
   {
      // Get VTS interface, module and channel
      IVTSystem vts = VTSystem.Instance;
      IVT2848 sensorModule1 = vts.GetChannel<IVT2848>("Sensor_Module1");
      IVT2848PWMStimChannel rpmSensor = vts.GetChannel<IVT2848PWMStimChannel>("RPM_Sensor");

      // The current value of the frequency (100Hz)
      double currentFrequency = 100.0;

      // Choose the source for high voltage on channels 1-4
      sensorModule1.OutputSource1To4.Value = OutputSource.VExt;

      // Choose a PWM curve
      rpmSensor.CurveType.Value = CurveType.PWM;
      // Set the number of repeats to unlimited
      rpmSensor.PWMRepeats.Value = 0;

      // Set initial frequency (100Hz) and duty cycle (50%) values
      rpmSensor.PWMOutputFreq.Value = currentFrequency;
      rpmSensor.PWMOutputDC.Value = 50.0;

      // Start the stimulation
      rpmSensor.StartStimulation();

      // To stimulate different sensor readings increase
      // frequency of the PWM signal over time
      while (currentFrequency < 200)
      {
         // Increase the frequency by 1Hz every 100ms
         Vector.CANoe.Threading.Execution.Wait(100);
         currentFrequency += 1;
         rpmSensor.PWMOutputFreq.Value = currentFrequency;
      }

      // Stop the stimulation
      rpmSensor.StopStimulation();
   }
<testcase title="SimulateSensorPWM" ident="">
      <vtsystem_configure title="Initialize PWM">
         <output_mode channel="VTS::RPM_Sensor" mode="low_side_switch" />
         <curve_type channel="VTS::RPM_Sensor" type="pwm" />
         <output_source channel="VTS::RPM_Sensor" source="v_ext" />
      </vtsystem_configure>
      <set title="Set frequency and duty cycle">
         <sysvar name="VTS::RPM_Sensor::PWMOutputDC">50.0</sysvar>
         <sysvar name="VTS::RPM_Sensor::PWMOutputFreq">100.0</sysvar>
      </set>
      <vtsystem_configure title="Start stimulation">
         <start_stimulation channel="VTS::RPM_Sensor" />
      </vtsystem_configure>
   </testcase>
```

## Availability

| Since Version |
|---|
