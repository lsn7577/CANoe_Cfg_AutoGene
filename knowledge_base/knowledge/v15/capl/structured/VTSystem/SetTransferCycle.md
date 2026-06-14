# SetTransferCycle

> Category: `VTSystem` | Type: `method`

## Syntax

```c
long SystemVariable.SetTransferCycle (double CycleTime);
```

## Description

Sets the cycle time for retrieving the measured value of a system variable from the VT System and writing it to the corresponding system variable.

## Parameters

| Name | Description |
|---|---|
| CycleTime | Defines the cycle time in seconds.The only available cycle times are 1 ms (= 0,001), 2 ms, 5 ms, 10 ms, 20 ms, 50 ms, 100 ms, 200 ms, 500 ms, 1 s, 2 s, 5 s and 10 s. Please note that not all cycle times are available for all measurement values. See possible settings in the VT System configuration dialog.If an invalid cycle time is specified, the call will fail with a feedback value of -1. |

## Example

The following example demonstrates how to change the transfer cycle of a VT System system variable during the measurement. Here the transfer cycle is reduced to 1 ms while the function waits for the input signal to change. This allows for a fast reaction. After the event has occurred the transfer cycle is set back to 100 ms.

```c
testfunction WaitForECUSignalChange ()
{
   // Change transfer cycle to 1ms to allow fast reaction
   sysvar::VTS::ECU_Dout_1::CurBit.SetTransferCycle(0.001);

   // Wait for digital ECU output to rise
   while(1)
   {
      if(@sysvar::VTS::ECU_Dout_1::CurBit == 1) break;
      TestWaitForTimeOut(1);
   }

   // Change transfer cycle back to 100ms
   sysvar::VTS::ECU_Dout_1::CurBit.SetTransferCycle(0.1);
}
public void WaitForECUSignalChange()
   {
      // Get VTS interface and digital input channel
      IVTSystem vts = VTSystem.Instance;
      IVT2516Channel ecuDOut1 = vts.GetChannel("ECU_Dout_1") as IVT2516Channel;

      // Change transfer cycle to 1ms to allow fast reaction
      ecuDOut1.CurBit.TransferCycle = 0.001;

      // Wait for digital ECU output to change
      bool initialValue = ecuDOut1.CurBit.Value;
      while (ecuDOut1.CurBit.Value == initialValue)
         Vector.CANoe.Threading.Execution.Wait(1);

      // Change transfer cycle back to 100ms
      ecuDOut1.CurBit.TransferCycle = 0.1;
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
