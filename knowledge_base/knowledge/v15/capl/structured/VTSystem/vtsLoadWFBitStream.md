# vtsLoadWFBitStream

> Category: `VTSystem` | Type: `function`

## Syntax

```c
long vtsLoadWFBitStream (char Target[], char filepath[]);
```

## Description

The function loads a bit stream (a sequence of bit values) for the channel from the specified file.The bit stream is used to stimulate the ECU using a digital signal.

## Parameters

| Name | Description |
|---|---|
| Target | Name of the system variable/namespace that will be affected by this function call. |
| filepath | Path of the file containing the bit stream.The path can be given absolute or relative to the CANoe configuration. |

## Example

The following example demonstrates how to use the bit stream voltage output of a VT2516 channel for digital stimulation. In this example a bit stream is loaded from the file BitStream.TXT and played back on channel DOut. More details for the output of bit streams can be found on CANoe online help topics VT2516: Bit Stream Output and VT2848: Bit Stream Output.

```c
// Sample bit stream
001100110010101100
BitstreamOutput ()
{
   // Choose voltage stimulation and bitstream curve type
   vtsSetStimulationMode("VTS::DOut", 1);
   vtsSetCurveType("VTS::DOut", 3);

   // Set high and low state voltages (12V and 0V)
   vtsSetPWMVoltageHigh("VTS::DOut", 12.0);
   vtsSetPWMVoltageLow("VTS::DOut", 0.0);

   // Load bitstream (the contents of BitStream.TXT are listed below)
   vtsLoadWFBitStream("VTS::DOut", "C:\\BitStream.TXT");

   // Configure bitstream. Parameters:
   // TimeIncrement (time to hold each sample)       = 10µs
   // Pause (pause between two waveform repetitions) = 5ms
   // NumberOfRepeats (number of repetitions)        = 0 (unlimited)
   vtsSetWFParams("VTS::DOut", 0.0001, 0.005, 0);

   // Output the configured bitstream for 10 seconds
   vtsStartStimulation("VTS::DOut");
   TestWaitForTimeout(10000);
   vtsStopStimulation("VTS::DOut");
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
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.5 SP2 | 13.0 | — | — | 1.0 |
| Restricted To | — | Main method | Main method VT offline | — | — | Main method |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
