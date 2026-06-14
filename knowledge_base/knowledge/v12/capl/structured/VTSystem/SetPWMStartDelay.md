# SetPWMStartDelay

> Category: `VTSystem` | Type: `function`

## Syntax

```c
Long SysVarNamespace.SetPWMStartDelay (double StartDelay);
```

## Description

Sets the delay of the start for the output of PWM signals and curves. This function is supported by the modules VT2004 and VT2848.

## Return Values

0: Successful call

## Example

In the following example the PWM output of two VT2004 channels is simulating two sensors with PWM output. The SetPWMStartDelay command ensures that the PWM output on channel Sensor2 is starting 2ms later to produce the corresponding phase shift.

```c
// Set up PWM stimulation for sensor 1

// Set voltage stimulation mode
sysvar::VTS::Sensor1.SetStimulationMode(1);
// Set curve type PWM
sysvar::VTS::Sensor1.SetCurveType(1);
// Set the low voltage of the PWM signal to 10V
sysvar::VTS::Sensor1.SetPWMVoltageLow(10);
// Set the high voltage of the PWM signal to 14V
sysvar::VTS::Sensor1.SetPWMVoltageHigh(14);
// Set duty cycle to 40%
@sysvar::VTS::Sensor1::PWMDC = 40;
// Set frequency to 100Hz
@sysvar::VTS::Sensor1::PWMFreq = 100;

// Set up PWM stimulation for sensor 2

// Set voltage stimulation mode
sysvar::VTS::Sensor2.SetStimulationMode(1);
// Set curve type PWM
sysvar::VTS::Sensor2.SetCurveType(1);
// Set the low voltage of the PWM signal to 10V
sysvar::VTS::Sensor2.SetPWMVoltageLow(10);
// Set the high voltage of the PWM signal to 14V
sysvar::VTS::Sensor2.SetPWMVoltageHigh(14);
// Set duty cycle to 40%
@sysvar::VTS::Sensor2::PWMDC = 40;
// Set frequency to 100Hz
@sysvar::VTS::Sensor2::PWMFreq = 100;

// set a start delay of 2ms for Sensor2
// -> PWM signals have a slight phase shift
sysvar::VTS::Sensor2.SetPWMStartDelay( 0.02);

// Start stimulation
sysvar::VTS::Sensor1.StartStimulation();
sysvar::VTS::Sensor2.StartStimulation();
  <testgroup title="PWMStartDelay">
  <testcase title="PWM measurement example" ident="">
    <vtsystem_configure title="Set PWM parameters for Sensor 1">
      <stimulation_mode channel="Sensor1" mode="voltage"/>
      <curve_type channel="Sensor1" type="pwm"/>
      <pwm_voltage_low channel="Sensor1">10</pwm_voltage_low>
      <pwm_voltage_high channel="Sensor1">14</pwm_voltage_high>
    </vtsystem_configure>
    <initialize title="Set Frequency and Duty Cycle for Sensor 1" wait="5">
      <sysvar name="PWMFreq" namespace="VTS::Sensor1">100</sysvar>
      <sysvar name="PWMDC" namespace="VTS::Sensor1">40</sysvar>
    </initialize>
    <vtsystem_configure title="Set PWM parameters for Sensor 2">
      <stimulation_mode channel="Sensor2" mode="voltage"/>
      <curve_type channel="Sensor2" type="pwm"/>
      <pwm_voltage_low channel="Sensor2">10</pwm_voltage_low>
      <pwm_voltage_high channel="Sensor2">14</pwm_voltage_high>
    </vtsystem_configure>
    <initialize title="Set Frequency and Duty Cycle for Sensor 2" wait="5">
      <sysvar name="PWMFreq" namespace="VTS::Sensor2">100</sysvar>
      <sysvar name="PWMDC" namespace="VTS::Sensor2">40</sysvar>
    </initialize>
    <vtsystem_configure title="Start Stimulation">
      <start_stimulation channel="Sensor1"/>
      <start_stimulation channel="Sensor2" start_delay="0.002"/>
    </vtsystem_configure>
  </testcase>
</testgroup>
```

## Availability

| Since Version |
|---|
