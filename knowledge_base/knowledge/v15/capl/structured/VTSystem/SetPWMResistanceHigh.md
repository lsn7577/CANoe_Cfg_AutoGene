# SetPWMResistanceHigh

> Category: `VTSystem` | Type: `method`

## Syntax

```c
long SysVarNamespace.SetPWMResistanceHigh (double Resistance);
```

## Description

Specifies the resistance value of a high signal on PWM output in "Resistance output PWM" mode.

## Parameters

| Name | Description |
|---|---|
| Resistance | Resistance value in ohms.Resistance may have values from 1.0 (1 Ω) up to 250000.0 (250 kΩ). This range is only supported by channel 4 of the VT2004 module. The other channels can handle values from 10.0 (10 Ω) up to 150000.0 (150 kΩ).In special cases Resistance may be set to -1 on each channel to get infinite resistance. Values outside the hardware's possible range of values are rounded up to the next highest value or the highest or lowest possible value is used. |

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
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.0 SP5 | 13.0 | — | — | 1.0 |
| Restricted To | — | — | VT offline | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
