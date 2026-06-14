# SetOutputMode

> Category: `VTSystem` | Type: `method`

## Syntax

```c
long SysVarNamespace.SetOutputMode (eVTS2848OutputMode Mode);
```

## Description

Sets the mode for output on the channel.

## Parameters

| Name | Description |
|---|---|
| Mode | Modes of VT2848 module: Values see eVTS2848OutputMode |

## Example

The following example demonstrates how to use the PWM output of a VT2848 channel to simulate a PWM based sensor (e.g. a RPM sensor). The channel used in this example is called RPM_Sensor.

```c
SimulateSensorPWM ()
{
   // The current value of the frequency (100Hz)
   float currentFrequency = 100.0;

   // Choose ′low side switch′, PWM curve type and
   // Vext as source for high value
   sysvar::VTS::RPM_Sensor.SetOutputMode(eVTS2848OutputModeLowsideSwitch);
   sysvar::VTS::RPM_Sensor.SetCurveType(eVTSCurveTypePWM);
   sysvar::VTS::SensorModule1.SetOutputSource(eVTSOutputSourceGroupChannels1To4, eVTSOutputSourceVExt);

   // Set the number of repeats to unlimited
   sysvar::VTS::RPM_Sensor.SetPWMRepeats(0);

   // Set initial frequency (100Hz) and duty cycle (50%) values
   @sysvar::VTS::RPM_Sensor::PWMOutputFreq = currentFrequency;
   @sysvar::VTS::RPM_Sensor::PWMOutputDC = 50.0;

   // Start the stimulation
   sysvar::VTS::RPM_Sensor.StartStimulation();

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
   sysvar::VTS::RPM_Sensor.StopStimulation();
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
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.6 SP4 | 13.0 | — | — | 1.0 |
| Restricted To | — | — | VT offline | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
