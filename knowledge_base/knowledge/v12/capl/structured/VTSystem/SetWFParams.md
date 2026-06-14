# SetWFParams

> Category: `VTSystem` | Type: `function`

## Syntax

```c
long SysVarNamespace.SetWFParams (double timeIncrement, double pause, dword numOfRepeats);
```

## Description

The function configures the parameters for the output of a voltage or resistance curve or bitstream.

## Return Values

0: Successful call

## Example

The following example demonstrates how to use the waveform resistance output of a VT2004 channel to simulate a sensor. In the example a waveform called WaveForm.TXT is loaded and replayed on channel Temp_Sensor. More details on waveforms can be found on CANoe online help topic VT2004: Arbitrary Wave Forms.

```c
// Example of an arbitrary wave form for resistance stimulation
100
120 ; 2
140 ; 1
100
160 ; 4
100
SimulateSensorResistanceWF ()
{
   // Choose resistor stimulation and waveform curve type
   sysvar::VTS::Temp_Sensor.SetStimulationMode(3);
   sysvar::VTS::Temp_Sensor.SetCurveType(2);

   // Load waveform (the contents of waveform.TXT are listed below)
   sysvar::VTS::Temp_Sensor.LoadWFResistance("C:\\WaveForm.TXT");

   // Configure waveform. Parameters:
   // TimeIncrement (time to hold each sample)       = 65ms
   // Pause (pause between two waveform repetitions) = 2s
   // NumberOfRepeats (number of repetitions)        = 3
   sysvar::VTS::Temp_Sensor.SetWFParams(0.065, 2.0, 3);

   // Start stimulation with the previously configured waveform
   sysvar::VTS::Temp_Sensor.StartStimulation();
}
public void SimulateSensorResistanceWF()
   {
      // Get VTS interface and VT2004 channel
      IVTSystem vts = VTSystem.Instance;
      IVT2004Channel tempSensor = vts.GetChannel("Temp_Sensor") as IVT2004Channel;

      // Choose voltage stimulation and a constant curve type
      tempSensor.SetStimulationMode(StimulationMode.ResistanceLower, CurveType.AnalogWaveform);

      // Load waveform (the contents of waveform.TXT are listed below)
      tempSensor.LoadWFResistance("C:\\WaveForm.TXT");

      // Configure waveform. Parameters:
      // TimeIncrement (time to hold each sample)       = 65ms
      // Pause (pause between two waveform repetitions) = 2s
      // NumberOfRepeats (number of repetitions)        = 3
      tempSensor.SetWFParams(0.065, 2.0, 3);

      // Start stimulation with the previously configured waveform
      tempSensor.StartStimulation();
   }
<testcase title="SimulateSensorResistanceWF" ident="">
      <vtsystem_configure title="Initialize waveform">
         <stimulation_mode channel="VTS::Temp_Sensor" mode="resistor_lt" />
         <curve_type channel="VTS::Temp_Sensor" type="wave_form" />
         <load_wave_form channel="VTS::Temp_Sensor" type="resistor">C:\WaveForm.TXT</load_wave_form>
         <wave_form_params channel="VTS::Temp_Sensor" time_increment="0.065" pause="2.0" />
      </vtsystem_configure>
      <wait time="10" title="Wait 10ms" />
      <vtsystem_configure title="Start stimulation">
         <start_stimulation channel="VTS::Temp_Sensor" num_of_repeats="0" />
      </vtsystem_configure>
      <wait time="10000" title="Wait 10s" />
      <vtsystem_configure title="Stop stimulation">
         <stop_stimulation channel="VTS::Temp_Sensor" />
      </vtsystem_configure>
</testcase>
```

## Availability

| Since Version |
|---|
