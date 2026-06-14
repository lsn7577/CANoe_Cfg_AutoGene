# canDisturbanceTriggerEnable

> Category: `CANDisturbance` | Type: `function`

## Syntax

```c
long canDisturbanceTriggerEnable(long deviceID, canStressNGErrorFrameTrigger trigger, canStressNGFrameSequence sequence); //form 1
long canDisturbanceTriggerEnable(long deviceID, canDisturbanceErrorFrameTrigger trigger, canDisturbanceFrameSequence sequence, canStressNGTriggerRepetitions repetitions); //form 2
long canDisturbanceTriggerEnable(long deviceID, canDisturbanceErrorFrameTrigger trigger, canDisturbanceFrameSequence sequence, canDisturbanceTriggerRepetitions repetitions, dword flags); // form 3
```

## Description

Configures an error frame trigger and a user-defined frame-based output sequence on a CAN Disturbance Interface.

If the trigger condition is fulfilled, the frame based sequence is sent on the bus.

It is possible to configure the trigger for the error flag or the error delimiter.

The position within the error flag or delimiter is configurable.

A typical use case is to start sending a frame after the error delimiter.

## Parameters

| Name | Type | Description |
|---|---|---|
| deviceID |  | The unique device ID that is configured via the Network Hardware Configuration dialog for a CAN channel. |
| trigger |  | The frame trigger condition for the CAN Disturbance Interface to output the sequence. |
| sequence |  | The user-defined frame based sequence that is sent, if the external trigger is fulfilled. |
| repetitions |  | The trigger repetitions. If the trigger repetitions are not defined, the CAN Disturbance Interface uses default values. |
| Value | Trigger Enable | Description |
| 0x0 | Disabled | No digital input (DIN) is used as trigger enable for the trigger condition. |
| 0x1 | DIN0 Active_Low | If DIN0 is 0, the trigger is enabled |
| 0x2 | DIN0 Active_High | If DIN0 is 1, the trigger is enabled |
| 0x4 | DIN1 Active_Low | If DIN1 is 0, the trigger is enabled |
| 0x8 | DIN1 Active_High | If DIN1 is 1, the trigger is enabled |
| 0x10 | Inverted Trigger | 0: Inverted trigger is disabled 1: Inverted trigger is enabled |
| 0x20 | Rx Direction* | 0: Direction trigger is disabled 1: Direction trigger is enabled |
| 0x40 | Tx Direction* | 0: Direction trigger is disabled 1: Direction trigger is enabled |
| 0x80 | Missing Bit Trigger | Trigger also, trigger position is not included within frame. |

## Example

Example for form 1

Example for form 2

Example for form 3

```c
CanDisturbanceErrorFrameTrigger   errFrameTrigger;
CanDisturbanceFrameSequence       frameSequence;
message 0x100                     msgFrameSeq;
long                              result;

//create the frame sequence based on a message
frameSequence.SetMessage(deviceID, msgFrameSeq);

errFrameTrigger.ErrorFramePhase = @sysvar::CanDisturbance::Enums::ErrorFramePhase::ErrorFlag;
errFrameTrigger.Offset = 10;

result = canDisturbanceTriggerEnable(deviceID, errFrameTrigger, frameSequence);

if(result == 1)
{
  write("Error frame trigger configured.");
}
else
{
  write("Error by configuration of error frame trigger %d", result);
}
CanDisturbanceErrorFrameTrigger    errFrameTrigger;
CanDisturbanceFrameSequence        frameSequence;
CanDisturbanceTriggerRepetitions   repetitions;
message 0x100                      msgFrameSeq;
long                               result;

//create the frame sequence based on a message
frameSequence.SetMessage(deviceID, msgFrameSeq);

errFrameTrigger.ErrorFramePhase = @sysvar::CanDisturbance::Enums::ErrorFramePhase::ErrorFlag;
errFrameTrigger.Offset = 10;

//Define two repetitions and one cycle with a 1 ms hold off time
repetitions.Cycles = 1;
repetitions.HoldOffCycles = 1;
repetitions.HoldOffRepetitions = 1;
repetitions.Repetitions = 2;

result = canDisturbanceTriggerEnable(deviceID, errFrameTrigger, frameSequence, repetitions);

if(result == 1)
{
  write("Error frame trigger configured.");
}
else
{
  write("Error by configuration of error frame trigger %d", result);
}
CanDisturbanceErrorFrameTrigger    errFrameTrigger;
CanDisturbanceFrameSequence        frameSequence;
CanDisturbanceTriggerRepetitions   repetitions;
message 0x100                      msgFrameSeq;
long                               flags;
long                               result;

//create the frame sequence based on a message
frameSequence.SetMessage(deviceID, msgFrameSeq);

errFrameTrigger.ErrorFramePhase = @sysvar::CanDisturbance::Enums::ErrorFramePhase::ErrorFlag;
errFrameTrigger.Offset = 10;

//Define two repetitions and one cycle with a 1 ms hold off time
repetitions.Cycles = 1;
repetitions.HoldOffCycles = 1;
repetitions.HoldOffRepetitions = 1;
repetitions.Repetitions = 2;

//define trigger enable, if DIO0 is active high the trigger could be trigger
flags = @sysvar::CanDisturbance::Enums::TriggerEnable::DIN0ActiveHigh;
result = canDisturbanceTriggerEnable(deviceID, errFrameTrigger, frameSequence, repetitions, flags);

if(result == 1)
{
  write("Error frame trigger configured.");
}
else
{
  write("Error by configuration of error frame trigger %d", result);
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
