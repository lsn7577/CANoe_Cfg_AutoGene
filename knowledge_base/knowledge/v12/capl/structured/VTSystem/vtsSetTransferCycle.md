# vtsSetTransferCycle

> Category: `VTSystem` | Type: `function`

## Syntax

```c
long vtsSetTransferCycle (char Target[], double CycleTime);
```

## Description

Sets the cycle time for retrieving the measured value of a system variable from the VT System and writing it to the corresponding system variable.

## Return Values

0: Successful call

## Example

The following example demonstrates how to change the transfer cycle of a VT System system variable during the measurement. Here the transfer cycle is reduced to 1 ms while the function waits for the input signal to change. This allows for a fast reaction. After the event has occurred the transfer cycle is set back to 100 ms.

```c
testfunction WaitForECUSignalChange ()
{
   // Change transfer cycle to 1ms to allow fast reaction
   vtsSetTransferCycle("VTS::ECU_Dout_1::CurBit", 0.001);

   // Wait for digital ECU output to rise
   while(1)
   {
      if(@sysvar::VTS::ECU_Dout_1::CurBit == 1) break;
      TestWaitForTimeOut(1);
   }

   // Change transfer cycle back to 100ms
   vtsSetTransferCycle("VTS::ECU_Dout_1::CurBit", 0.1);
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
<testcase title="SetTransferCycle" ident="">
      <vtsystem_configure title="Set transfer cycle to 1ms">
         <transfer_cycle channel="VTS::ECU_Dout_1" sysvar="CurBit">0.001</transfer_cycle>
      </vtsystem_configure>
      <awaitvaluematch timeout="5000" title="Wait for input value to go to 1">
         <sysvar name="VTS::ECU_Dout_1::CurBit">1</sysvar>
      </awaitvaluematch>
      <completion>
         <vtsystem_configure title="Set transfer cycle to back to 100ms">
            <transfer_cycle channel="VTS::ECU_Dout_1" sysvar="CurBit">0.1</transfer_cycle>
         </vtsystem_configure>
      </completion>
   </testcase>
```

## Availability

| Since Version |
|---|
