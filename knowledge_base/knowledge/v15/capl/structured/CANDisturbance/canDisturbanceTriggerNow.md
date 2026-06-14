# canDisturbanceTriggerNow

> Category: `CANDisturbance` | Type: `method`

## Syntax

```c
long canDisturbanceTriggerNow(long deviceID, canDisturbanceSequence); // form 1
long canDisturbanceTriggerNow(long deviceID, canDisturbanceSequence, canDisturbanceTriggerRepetitions repetitions);// form 2
long canDisturbanceTriggerNow(long deviceID, canDisturbanceFrameSequence sequence); // form 3
long canDisturbanceTriggerNow(long deviceID, canDisturbanceFrameSequence sequence, canDisturbanceTriggerRepetitions repetitions); // form 4
```

## Description

Sends a user-defined sequence or a frame-based sequence on the bus with the CAN Disturbance Interface.

The sequence or frame-based sequence sends directly on the bus. If a frame is currently sent by another interface, this frame will be disturbed.

A typical use case is to send a sequence or a frame based sequence on the bus without any trigger conditions.

## Parameters

| Name | Description |
|---|---|
| deviceID | The unique device ID configured via the Network Hardware Configuration dialog for a CAN channel. |
| sequence | The user-defined sequence or frame based sequence. |
| repetitions | The repetitions of the output sequence. |

## Example

Example for form 1

Example for form 2

Example for form 3

Example for form 4

```c
CanDisturbanceSequence   sequence;
long                     result;

//Clear sequence
sequence.Clear();

//configure a sequence one bit long and send a dominant bit
result = sequence.AppendToSequence(320, 'd');

if(result == 1)
{
  result= canDisturbanceTriggerNow(deviceID, sequence);

  if(result == 1)
  {
    write("Trigger now is configured.");
  }
  else
  {
    write("Error by configuration of trigger now %d", result);
  }
}
CanDisturbanceSequence             sequence;
CanDisturbanceTriggerRepetitions   repetitions;
long                               result;

//Clear sequence
sequence.Clear();

//configure a sequence one bit long and send a dominant bit
result = sequence.AppendToSequence(320, 'd');

if(result == 1)
{
  //Define two repetitions and one cycle with a 1 ms hold off time
  repetitions.Cycles = 1;
  repetitions.HoldOffCycles = 1;
  repetitions.HoldOffRepetitions = 1;
  repetitions.Repetitions = 2;

  result= canDisturbanceTriggerNow(deviceID, sequence, repetitions);

  if(result == 1)
  {
    write("Trigger now is configured.");
  }
  else
  {
    write("Error by configuration of trigger now %d", result);
  }
}
canDisturbanceFrameSequence   frameSequence;
message 0x100                 msgFrameSeq;
long                          result;

//set message to sequence
frameSequence.SetMessage(deviceID, msgFrameSeq);
result = canDisturbanceTriggerNow(deviceID, frameSequence);

if(result == 1)
{
  write("Trigger now is configured.");
}
else
{
  write("Error by configuration of trigger now %d", result);
}
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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 10.0 10.0 SP3 recommended | — | — | — | 2.2 |
| Restricted To | — | CAN CAN Disturbance Interface | — | — | — | CAN CAN Disturbance Interface |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
