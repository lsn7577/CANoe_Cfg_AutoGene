# canDisturbanceTriggerNow

> Category: `CANDisturbance` | Type: `function`

## Syntax

```c
long canDisturbanceTriggerNow (long deviceID, canDisturbanceSequence); // form 1
```

## Description

Sends a user-defined sequence or a frame-based sequence on the bus with the CAN Disturbance Interface.

The sequence or frame-based sequence sends directly on the bus. If a frame is currently sent by another interface, this frame will be disturbed.

A typical use case is to send a sequence or a frame based sequence on the bus without any trigger conditions.

## Return Values

1: Success

## Example

```c
canDisturbanceFrameSequence        frameSequence;
canDisturbanceTriggerRepetitions   repetitions;
message 0x100                      msgFrameSeq;
long                               result;

//set message to sequence
frameSequence.SetMessage(deviceID, msgFrameSeq);

//Define two repetitions and one cycle with a 1 ms hold off time
repetitions.Cycles = 1;
repetitions.HoldOffCycles = 1;
repetitions.HoldOffRepetitions = 1;
repetitions.Repetitions = 2;

//output the sequence twice
result = canDisturbanceTriggerNow(deviceID, frameSequence, repetitions);

if(result == 1)
{
  write("Trigger now is configured.");
}
else
{
  write("Error by configuration of trigger now %d", result);
}
```

## Availability

| Since Version |
|---|
