# SetStimulationMode

> Category: `VTSystem` | Type: `function`

## Syntax

```c
long SysVarNamespace.SetStimulationMode (eVTSStimulationMode Mode);
```

## Description

Sets the mode for internal voltage or resistance stimulation.

## Return Values

0: Successful call

## Example

The following example demonstrates how to use the PWM output of a VT2004 channel to simulate a PWM based sensor (e.g. a RPM sensor). The channel used in this example is called RPM_Sensor.

```c
SimulateSensorPWM ()
{
   // The current value of the frequency (100Hz)
   float currentFrequency = 100.0;

   // Choose voltage stimulation and a PWM curve type
   sysvar::VTS::RPM_Sensor.SetStimulationMode(eVTSStimulationModeVoltage);
   sysvar::VTS::RPM_Sensor.SetCurveType(eVTSCurveTypePWM);

   // PWM signal will toggle between 0V and 5V
   sysvar::VTS::RPM_Sensor.SetPWMVoltageLow(0.0);
   sysvar::VTS::RPM_Sensor.SetPWMVoltageHigh(5.0);

   // Set the number of repeats to unlimited
   sysvar::VTS::RPM_Sensor.SetPWMRepeats(0);

   // Set initial frequency (100Hz) and duty cycle (50%) values
   @sysvar::VTS::RPM_Sensor::PWMFreq = currentFrequency;
   @sysvar::VTS::RPM_Sensor::PWMDC = 50.0;

   // Start the stimulation
   sysvar::VTS::RPM_Sensor.StartStimulation();

   // To stimulate different sensor readings increase
   // frequency of the PWM signal over time
   while(currentFrequency < 200)
   {
      // Increase the frequency by 1Hz every 100ms
      TestWaitForTimeOut(100);
      currentFrequency += 1;
      @sysvar::VTS::RPM_Sensor::PWMFreq = currentFrequency;
   }

   // Stop the stimulation
   sysvar::VTS::RPM_Sensor.StopStimulation();
}
public void SimulateSensorPWM()
   {
   // Get VTS interface and VT2004 channel
   IVTSystem vts = VTSystem.Instance;
   IVT2004Channel rpmSensor = vts.GetChannel("RPM_Sensor") as IVT2004Channel;

   // The current value of the frequency (100Hz)
   double currentFrequency = 100.0;

   // Choose voltage stimulation and a PWM curve type
   rpmSensor.SetStimulationMode(StimulationMode.Voltage, CurveType.PWM);

   // PWM signal will toggle between 0V and 5V
   rpmSensor.PWMVoltageLow.Value = 0.0;
   rpmSensor.PWMVoltageHigh.Value = 5.0;

   // Set the number of repeats to unlimited
   rpmSensor.PWMRepeats.Value = 0;

   // Set initial frequency (100Hz) and duty cycle (50%) values
   rpmSensor.PWMFreq.Value = currentFrequency;
   rpmSensor.PWMDC.Value = 50.0;

   // Start the stimulation
   rpmSensor.StartStimulation();

   // To stimulate different sensor readings increase
   // frequency of the PWM signal over time
   while(currentFrequency < 200)
   {
      // Increase the frequency by 1Hz every 100ms
      Vector.CANoe.Threading.Execution.Wait(100);
      currentFrequency += 1;
      rpmSensor.PWMFreq.Value = currentFrequency;
   }

   // Stop the stimulation
   rpmSensor.StopStimulation();
}
<testcase title="SimulateSensorPWM" ident="">
      <vtsystem_configure title="Initialize PWM">
         <stimulation_mode channel="VTS::RPM_Sensor" mode="voltage" />
         <curve_type channel="VTS::RPM_Sensor" type="pwm" />
         <pwm_voltage_low channel="VTS::RPM_Sensor">0.0</pwm_voltage_low>
         <pwm_voltage_high channel="VTS::RPM_Sensor">5.0</pwm_voltage_high>
      </vtsystem_configure>
      <set title="Set frequency and duty cycle">
         <sysvar name="VTS::RPM_Sensor::PWMDC">50.0</sysvar>
         <sysvar name="VTS::RPM_Sensor::PWMFreq">100.0</sysvar>
      </set>
      <vtsystem_configure title="Start stimulation">
         <start_stimulation channel="VTS::RPM_Sensor" />
      </vtsystem_configure>
   </testcase>
```

## Availability

| Since Version |
|---|
