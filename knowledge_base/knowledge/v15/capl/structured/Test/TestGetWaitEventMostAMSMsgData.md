# TestGetWaitEventMostAMSMsgData

> Category: `Test` | Type: `function`

## Syntax

```c
long TestGetWaitEventMostAMSMsgData (MostAMSmessage aMessage); // form 1
long TestGetWaitEventMostAMSMsgData (dword index, MostAMSmessage aMessage); // form 2
```

## Description

If the last event was a MOST AMS message that resolved a wait construction, with the first function the content of the message can be called.The second function can only be used for "joined events". The number of the "joined event" (return value of "testJoin…") is here being used as an index.

## Parameters

| Name | Description |
|---|---|
| aMessage | Message variable that should be filled in with this function. |
| index | Number of the "joined event" corresponds with the return value of "testJoin...". |

## Example

```c
if(testWaitForMostAMSMessage("AudioDiskPlayer.MediaInfo.Status", 1, 500) == 1)
  {
    mostAMSMessage * msg;
    testGetWaitEventMostAMSMsgData(msg);
    if(msg.DLC > 4 && msg.byte(4) == 1)
    {
      testStepPass("MediaType = Audio");
    }
    else
    {
      testStepFail();
    }
  }
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.0: form 1 6.0: form 2 | 13.0 | — | — | — |
| Restricted To | — | MOST25, MOST50, MOST150 | MOST25, MOST50, MOST150 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
