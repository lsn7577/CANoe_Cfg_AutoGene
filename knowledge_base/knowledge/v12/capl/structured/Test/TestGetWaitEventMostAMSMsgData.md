# TestGetWaitEventMostAMSMsgData

> Category: `Test` | Type: `function`

## Syntax

```c
long TestGetWaitEventMostAMSMsgData (MostAMSmessage aMessage);
```

## Description

If the last event was a MOST AMS message that resolved a wait construction, with the first function the content of the message can be called.The second function can only be used for "joined events". The number of the "joined event" (return value of "testJoin…") is here being used as an index.

## Return Values

0: Successful data access

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

| Since Version |
|---|
