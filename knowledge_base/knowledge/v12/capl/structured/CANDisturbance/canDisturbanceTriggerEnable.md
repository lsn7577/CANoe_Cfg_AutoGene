# canDisturbanceTriggerEnable

> Category: `CANDisturbance` | Type: `function`

## Syntax

```c
long canDisturbanceTriggerEnable (long deviceID, canDisturbanceFrameTrigger trigger, canDisturbanceSequence sequence); // form 1
```

## Description

Configures a frame trigger and a user-defined output sequence on a CAN Disturbance Interface.

When the trigger condition is fulfilled, the CAN Disturbance Interface starts sending the given sequence on the bus. The starting point of the sequence can be configured by the canDisturbanceFrameTrigger parameter.

A typical use case for this function is to send a sequence within a CAN frame, to disturb a single bit or a range of bits.

Constraints

If the level of the trigger bit must be a specific level (dominant or recessive), the value of the bit is measured at the sample point. If the margin sync time (MST) between sample point and the start of the next bit is smaller than the delay time (DT) that is needed to send the sequence on the bus, the sequence is not synchronized to the start of the next bit.

## Return Values

1: Success

## Example

```c
CanDisturbanceFrameTrigger         frameTrigger;
CanDisturbanceSequence             sequence;
CanDisturbanceTriggerRepetitions   repetitions;
long                               result;
long                               validityMask;
message 0x100x                     triggerMessage;
dword                              flags;

//clear the sequence
sequence.Clear();
//configure the message should be triggered

//ID must extended ID and a CAN message must on the bus
validityMask = @sysvar::CanDisturbance::Enums::ValidityMaskFlags::IDBase
               | @sysvar::CanDisturbance::Enums::ValidityMaskFlags::IDExtended
               | @sysvar::CanDisturbance::Enums::ValidityMaskFlags::IDE
               | @sysvar::CanDisturbance::Enums::ValidityMaskFlags::FDF;

frameTrigger.SetMessage(triggerMessage, deviceID, validityMask);
//trigger position is the ACK Slot
frameTrigger.TriggerFieldType =
               @sysvar::CanDisturbance::Enums::FieldType::ACKSlot;
frameTrigger.TriggerFieldOffset = 0;

//configure a sequence 320 FPGA ticks long and send a dominant bit at the Ack Delimiter bit on the bus. A FPGA tick is 6.25 ns long, which leads to a bit time of 2 µs
result = sequence.AppendToSequence(320, 'd');

//Define 33 repetitions and one cycle with a 1 ms hold off time
repetitions.Cycles = 1;
repetitions.HoldOffCycles = 1;
repetitions.HoldOffRepetitions = 0;
repetitions.Repetitions = 33;

//define trigger enable, if DIO0 is active high the trigger could be trigger
flags = @sysvar::CanDisturbance::Enums::TriggerEnable::DIN0ActiveHigh;

//Configure the frame trigger and the sequence to the CAN Disturbance Interface
if(result == 1)
{
  result = canDisturbanceTriggerEnable(deviceID, frameTrigger,
  sequence, repetitions, flags);
  if(result == 1)
  {
    write("Trigger is enabled");
  }
  else
  {
    write("Enable trigger error Result =%d", result);
  }
}
```

## Availability

| Since Version |
|---|
