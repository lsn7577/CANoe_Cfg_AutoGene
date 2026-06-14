# vtsSetStimulationMode

> Category: `VTSystem` | Type: `function`

## Syntax

```c
long vtsSetStimulationMode (char Target[],eVTSStimulationMode Mode);
```

## Description

Sets the mode for internal voltage or resistance stimulation.

## Parameters

| Name | Description |
|---|---|
| Target | Name of the system variable/namespace that will be affected by this function call. |
| Mode | Values see eVTSStimulationMode |

## Example

The following example demonstrates how to use the PWM output of a VT2004 channel to simulate a PWM based sensor (e.g. a RPM sensor). The channel used in this example is called RPM_Sensor.

```c
SimulateSensorPWM ()
{
   // The current value of the frequency (100Hz)
   float currentFrequency = 100.0;

   // Choose voltage stimulation and a PWM curve type
   vtsSetStimulationMode("VTS::RPM_Sensor", eVTSStimulationModeVoltage);
   vtsSetCurveType("VTS::RPM_Sensor", eVTSCurveTypePWM);

   // PWM signal will toggle between 0V and 5V
   vtsSetPWMVoltageLow("VTS::RPM_Sensor", 0.0);
   vtsSetPWMVoltageHigh("VTS::RPM_Sensor", 5.0);

   // Set the number of repeats to unlimited
   vtsSetPWMRepeats("VTS::RPM_Sensor", 0);

   // Set initial frequency (100Hz) and duty cycle (50%) values
   @sysvar::VTS::RPM_Sensor::PWMFreq = currentFrequency;
   @sysvar::VTS::RPM_Sensor::PWMDC = 50.0;

   // Start the stimulation
   vtsStartStimulation("VTS::RPM_Sensor");

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
   vtsStopStimulation("VTS::RPM_Sensor");
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
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.5 SP2 | 13.0 | — | — | 1.0 |
| Restricted To | — | — | VT offline | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
