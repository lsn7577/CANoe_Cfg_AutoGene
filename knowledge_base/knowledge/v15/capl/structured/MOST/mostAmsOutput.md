# mostAmsOutput

> Category: `MOST` | Type: `function`

## Syntax

```c
mostAmsOutput(long channel, long destAdr, char symbolicMessage[], long instId); // form 1
mostAmsOutput(long channel, char symbolicMessage[], long instId); // form 2
mostAmsOutput(long channel, char symbolicMessage[]); // form 3
```

## Description

Definition and direct dispatch of an AMS message using the syntax from the MOST specification and the description in the XML function catalog.

The description of the message must be complete, i.e. wildcards cannot be used because the message should then be sent directly. However, the parameter list may be shorter than specified in the function catalog, in order to be able to generate intentionally incomplete messages.

## Parameters

| Name | Description |
|---|---|
| channel | Channel of the connected interface. |
| destAdr | Destination address. |
| symbolicMessage | Description of the message content in the following formats: FBlock.InstanceId.Function.OpType(Parameterlist) FBlock.InstanceId.Function.OpType FBlock.Function.OpType(Parameterlist) FBlock.Function.OpType |
| InstId | InstanceID of the function block. This explicit entry overwrites the applicable InstanceID in symbolicMessage. If neither an instance ID nor the instId parameter is specified in symbolicMessage, the default is set to 1. |

## Return Values

—

## Example

```c
// send 'play' command 
 for DiskPlayer on MOST ring
on key 'p'
{
   // Send command on channel 1 to instanceId 1 of functionblock "AudioDiskPlayer"
   mostAmsOutput(1,"AudioDiskPlayer.SourceActivity.StartResult(1,On)",1);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.2 | 5.2 | — | — | — | —✔ |
| Restricted To | MOST25 MOST50 MOST150 | MOST25 MOST50 MOST150 | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
