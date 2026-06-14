# LoadWFBitStream

> Category: `VTSystem` | Type: `function`

## Syntax

```c
long SysVarNamespace.LoadWFBitStream (char filepath[]);
```

## Description

The function loads a bit stream (a sequence of bit values) for the channel from the specified file.The bit stream is used to stimulate the ECU using a digital signal.

## Return Values

0: Successful call

## Example

The following example demonstrates how to use the bit stream voltage output of a VT2516 channel for digital stimulation. In this example a bit stream is loaded from the file BitStream.TXT and played back on channel DOut. More details for the output of bit streams can be found on CANoe online help topics VT2516: Bit Stream Output and VT2848: Bit Stream Output.

```c
// Sample bit stream
001100110010101100
BitstreamOutput ()
{
   // Choose voltage stimulation and bitstream curve type
   sysvar::VTS::DOut.SetStimulationMode(1);
   sysvar::VTS::DOut.SetCurveType(3);

   // Set high and low state voltages (12V and 0V)
   sysvar::VTS::DOut.SetPWMVoltageHigh(12.0);
   sysvar::VTS::DOut.SetPWMVoltageLow(0.0);

   // Load bitstream (the contents of BitStream.TXT are listed below)
   sysvar::VTS::DOut.LoadWFBitStream("C:\\BitStream.TXT");

   // Configure bitstream. Parameters:
   // TimeIncrement (time to hold each sample)       = 10µs
   // Pause (pause between two waveform repetitions) = 5ms
   // NumberOfRepeats (number of repetitions)        = 0 (unlimited)
   sysvar::VTS::DOut.SetWFParams(0.0001, 0.005, 0);

   // Output the configured bitstream for 10 seconds
   sysvar::VTS::DOut.StartStimulation();
   TestWaitForTimeout(10000);
   sysvar::VTS::DOut.StopStimulation();
}
public void BitstreamOutput()
   {
      // Get VTS interface and VT2516 channel
      IVTSystem vts = VTSystem.Instance;
      IVT2516Channel digiOut = vts.GetChannel("DOut") as IVT2516Channel;

      // Choose voltage stimulation and bitstream curve type
      digiOut.SetStimulationMode(StimulationMode.Voltage, CurveType.BitStream);

      // Set high and low state voltages (12V and 0V)
      digiOut.PWMVoltageHigh.Value = 12.0f;
      digiOut.PWMVoltageLow.Value = 0.0f;

      // Load bitstream (the contents of BitStream.TXT are listed below)
      digiOut.LoadWFBitStream("C:\\BitStream.TXT");

      // Configure bitstream. Parameters:
      // TimeIncrement (time to hold each sample)       = 10µs
      // Pause (pause between two waveform repetitions) = 5ms
      // NumberOfRepeats (number of repetitions)        = 0 (unlimited)
      digiOut.SetWFParams(0.0001, 0.005, 0);

      // Output the configured bitstream for 10 seconds
      digiOut.StartStimulation();
      Vector.CANoe.Threading.Execution.Wait(10000);
      digiOut.StopStimulation();
   }
<testcase title="BitstreamOutput" ident="">
      <vtsystem_configure title="Initialize bitstream output">
         <stimulation_mode channel="VTS::DOut" mode="voltage" />
         <curve_type channel="VTS::DOut" type="bit_stream" />
         <pwm_voltage_low channel="VTS::DOut">0.0</pwm_voltage_low>
         <pwm_voltage_high channel="VTS::DOut">12.0</pwm_voltage_high>
         <load_wave_form channel="VTS::DOut" type="bit_stream">c:\BitStream.TXT</load_wave_form>
         <wave_form_params channel="VTS::DOut" time_increment="0.0001" pause="0.005" />
      </vtsystem_configure>
      <wait time="10" title="Wait 10ms" />
      <vtsystem_configure title="Start stimulation">
         <start_stimulation channel="VTS::DOut" num_of_repeats="0" />
      </vtsystem_configure>
      <wait time="10000" title="Wait 10s" />
      <vtsystem_configure title="Stop stimulation">
         <stop_stimulation channel="VTS::DOut" />
      </vtsystem_configure>
   </testcase>
```

## Availability

| Since Version |
|---|
