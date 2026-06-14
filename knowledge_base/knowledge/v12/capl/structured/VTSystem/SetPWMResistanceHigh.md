# SetPWMResistanceHigh

> Category: `VTSystem` | Type: `function`

## Syntax

```c
long SysVarNamespace.SetPWMResistanceHigh (double Resistance);
```

## Description

Specifies the resistance value of a high signal on PWM output in "Resistance output PWM" mode.

## Return Values

0: Successful call

## Example

The following example demonstrates how to use the internal resistor decade of a VT2004 channel to simulate a PWM based sensor. On channel Temp_Sensor the resistor is toggled between 100 Ohm and 140 Ohm with a frequency of 20 Hz and a duty cycle of 50%.

```c
SimulateSensorPWMResistance ()
{
   // Choose resistor stimulation and a PWM curve type
   sysvar::VTS::Temp_Sensor.SetStimulationMode(3);
   sysvar::VTS::Temp_Sensor.SetCurveType(1);

   // Configure low (100Ohm) and high (140Ohm) resistance values
   sysvar::VTS::Temp_Sensor.SetPWMResistanceLow(100);
   sysvar::VTS::Temp_Sensor.SetPWMResistanceHigh(140);

   // Set the number of repeats to unlimited
   sysvar::VTS::Temp_Sensor.SetPWMRepeats(0);

   // Create a PWM signal with frequency 20Hz and DC 50%
   @sysvar::VTS::Temp_Sensor::PWMFreq = 20.0;
   @sysvar::VTS::Temp_Sensor::PWMDC = 50.0;

   // Start the stimulation
   sysvar::VTS::Temp_Sensor.StartStimulation();
}
public void SimulateSensorPWMResistance()
   {
      // Get VTS interface and VT2004 channel
      IVTSystem vts = VTSystem.Instance;
      IVT2004Channel tempSensor = vts.GetChannel("Temp_Sensor") as IVT2004Channel;

      // Choose resistor stimulation and a PWM curve type
      tempSensor.SetStimulationMode(StimulationMode.ResistanceLower, CurveType.PWM);

      // Configure low (100Ohm) and high (140Ohm) resistance values
      tempSensor.PWMResistanceLow.Value = 100.0;
      tempSensor.PWMResistanceHigh.Value = 140.0;

      // Set the number of repeats to unlimited
      tempSensor.PWMRepeats.Value = 0;

      // Start the stimulation
      tempSensor.StartStimulation();

      // Create a PWM signal with frequency 20Hz and DC 50%
      tempSensor.PWMFreq.Value = 20.0;
      tempSensor.PWMDC.Value = 50.0;
   }
<testcase title="SimulateSensorPWMResistance" ident="">
      <vtsystem_configure title="Initialize PWM">
         <stimulation_mode channel="VTS::Temp_Sensor" mode="resistor_gt" />
         <curve_type channel="VTS::Temp_Sensor" type="pwm" />
         <pwm_resistance_low channel="VTS::Temp_Sensor">100</pwm_resistance_low>
         <pwm_resistance_high channel="VTS::Temp_Sensor">140</pwm_resistance_high>
      </vtsystem_configure>
      <set title="Set frequency and duty cycle">
         <sysvar name="VTS::RPM_Sensor::PWMDC">50.0</sysvar>
         <sysvar name="VTS::RPM_Sensor::PWMFreq">20</sysvar>
      </set>
      <wait time="10" title="Wait 10ms" />
      <vtsystem_configure title="Start stimulation">
         <start_stimulation channel="VTS::Temp_Sensor" />
      </vtsystem_configure>
   </testcase>
```

## Availability

| Since Version |
|---|
