# vtsLoadWFVoltage

> Category: `VTSystem` | Type: `function`

## Syntax

```c
long vtsLoadWFVoltage (char Target[], char filepath[]);
```

## Description

The function loads a voltage curve for the channel from the specified file.

## Parameters

| Name | Description |
|---|---|
| Target | Name of the system variable/namespace that will be affected by this function call. |
| filepath | Path of the file containing the voltage curve. The path can be given absolute or relative to the CANoe configuration. |

## Example

The following example demonstrates how to use the waveform voltage output of a VT2004 channel to simulate a sensor. In the example a waveform called WaveForm.TXT is loaded and replayed on channel Temp_Sensor. More details on waveforms can be found on CANoe online help topic VT2004: Arbitrary Wave Forms.

The second part of the example shows how a waveform can be output on a VT7001 power supply channel. An external power supply unit (namespace ExtSupply) is used in this example. The ECU is connected to OUT1 (namespace ECUpower) and GND1; the VT7001 module is named Power-Supply. The output voltage is determined by a predefined curve (powercycle.TXT). The time increment for the curve's interpolation points is 65 ms; the curve is for 10 seconds.

```c
// Example of an arbitrary wave form
0 // Next value is an interpolation point
1.0; 2 // Two sampling points lie between the next interpolation point
4
2 // Also possible
3; 1
1; 1
2
SimulateSensorVoltageWF ()
{
   // Choose voltage stimulation and waveform curve type
   vtsSetStimulationMode("VTS::Temp_Sensor", 1);
   vtsSetCurveType("VTS::Temp_Sensor", 2);

   // Load waveform (the contents of WaveForm.TXT are listed below)
   vtsLoadWFVoltage("VTS::Temp_Sensor", "C:\\WaveForm.TXT");

   // Configure waveform. Parameters:
   // TimeIncrement (time to hold each sample)       = 65ms
   // Pause (pause between two waveform repetitions) = 2s
   // NumberOfRepeats (number of repetitions)        = 0 (unlimited)
   vtsSetWFParams("VTS::Temp_Sensor", 0.065, 2.0, 0);

   // Output the configured waveform for 10 seconds
   vtsStartStimulation("VTS::Temp_Sensor");
   TestWaitForTimeout(10000);
   vtsStopStimulation("VTS::Temp_Sensor");
}
ExternalSupplyWithCurve ()
{
   // Set mode to one power supply only -> external power supply 1
   vtsSetInterconnectionMode("VTS::PowerSupply", 1);

   // Load waveform from file
   // Factor is set to 0.2: 1 V control voltage -> 5 V output at power supply
   vtsSetRefVoltageMode("VTS::ExtSupply", 2, 0.2);
   vtsLoadWFVoltage("VTS::ExtSupply", "powercycle.TXT");
   vtsSetWFParams("VTS::ExtSupply", 0.00005, 0.2, 0);

   // Switch outputs on and start output curve
   @sysvar::VTS::Clamp30::Active = 1;
   vtsStartStimulation("VTS::ExtSupply");

   // Wait for 5 seconds, the stop the curve playback
   TestWaitForTimeOut(5000);
   vtsStopStimulation("VTS::ExtSupply");
}
public void SimulateSensorVoltageWF()
   {
      // Get VTS interface and VT2004 channel
      IVTSystem vts = VTSystem.Instance;
      IVT2004Channel tempSensor = vts.GetChannel("Temp_Sensor") as IVT2004Channel;

      // Choose voltage stimulation and a constant curve type
      tempSensor.SetStimulationMode(StimulationMode.Voltage, CurveType.AnalogWaveform);

      // Load waveform (the contents of waveform.TXT are listed below)
      tempSensor.LoadWFVoltage("C:\\WaveForm.TXT");

      // Configure waveform. Parameters:
      // TimeIncrement (time to hold each sample)       = 65ms
      // Pause (pause between two waveform repetitions) = 2s
      // NumberOfRepeats (number of repetitions)        = 0 (unlimited)
      tempSensor.SetWFParams(0.065, 2.0, 0);

      // Output the configured waveform for 10 seconds
      tempSensor.StartStimulation();
      Vector.CANoe.Threading.Execution.Wait(10000);
      tempSensor.StopStimulation();
   }
public void ExternalSupplyWithCurve()
   {
      // Get VTS interface, VT7001 module, external supply and output channel
      IVTSystem vts = VTSystem.Instance;
      IVT7001 powerSupply = vts.GetModule("PowerSupply") as IVT7001;
      IVT7001SupplyExternal extSupply = vts.GetChannel("ExtSupply") as IVT7001SupplyExternal;
      IVT7001Channel clamp30 = vts.GetChannel("Clamp30") as IVT7001Channel;

      // Set mode to one power supply only -> external power supply 1
      powerSupply.InterconnectionMode.Value = InterconnectionMode.Sup1;

      // Load waveform from file
      // Factor is set to 0.2: 1 V control voltage -> 5 V output at power supply
      extSupply.SetRefVoltageMode(RefVoltageMode.AnalogWaveForm, 0.2);
      extSupply.LoadWFVoltage("powercycle.TXT");
      extSupply.SetWFParams(0.00005, 0.2, 0);

      // Switch outputs on and start output curve
      clamp30.Active.Value = OutputMode.Active;
      extSupply.StartStimulation();

      // Wait for 5 seconds, the stop the curve playback
      Vector.CANoe.Threading.Execution.Wait(5000);
      extSupply.StopStimulation();
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
