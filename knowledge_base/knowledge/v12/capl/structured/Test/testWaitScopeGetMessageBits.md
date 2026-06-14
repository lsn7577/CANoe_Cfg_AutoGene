# testWaitScopeGetMessageBits

> Category: `Test` | Type: `function`

## Syntax

```c
long testWaitScopeGetMessageBits(message msg, ScopeAnalysisSetup setup, dword arraySize, scopeBitData signalData1[], scopeBitData signalData2[], scopeBitData signalData3[]);
```

## Description

A CAN message stored in the scope buffer will be parsed. For each bit of the message the signal voltage levels, the bit length, and the bit type will be returned.

## Return Values

1 = success

## Example

```c
dword arraySize = 200;
message 0x111 msg1;
long res;
long evtNo;
ScopeBitData data1[200];
ScopeBitData data2[200];
ScopeBitData data3[200];
ScopeAnalysisSetup setupAnalyse;

//------------------------------
//Connect to scope
//------------------------------
res = scopeConnect();
res = testWaitForScopeEvent(eScopeConnected, 8000);

if(res > 0)
{
  testStep("Wait For Event", "Waiting for Message 0x111");
  testJoinMessageEvent(msg1.id);
  evtNo = TestWaitForAnyJoinedEvent(2000);
  res = TestGetWaitEventMsgData(msg1);

  if(res != 0)
  {
    testStepFail("Wait For Event", "No event received");
    res = scopeDisconnect();
    res =testWaitForScopeEvent(eScopeDisconnected, 8000);
    return;
  }
  else
  {
    testStepPass("Wait For Event", "Event received");
  }

res = scopeTriggerNow();
if(res > 0)
  {
    res =(testWaitForScopeEvent(eScopeTriggered, 5000));

    if(res > 0)
    {
      setupAnalyse.samplePoint = 70;
      res = testWaitScopeGetMessageBits(msg1, setupAnalyse, arraySize, data1, data2, data3);

      if(res > 0 || res == -105)
      {
        int i;
        for(i = 0; i < arraySize;++i)
          {
            write("CANH: StarTime%.6f s, Type: %d, TypeExt: %d, BitLength: %d, Voltage: %.6f, BitValue: %d", data1[i].StartTime /1000000000., data1[i].type, data1[i].typeEx, data1[i].bitLength, data1[i].signalVoltage,data1[i].bitValue);
            write("CANL: StarTime%.6f s, Type: %d, TypeExt: %d, BitLength: %d, Voltage: %.6f, BitValue: %d", data2[i].StartTime /1000000000., data2[i].type, data2[i].typeEx, data2[i].bitLength, data2[i].signalVoltage,data2[i].bitValue);
            write("CANDiff: StarTime%.6f s, Type: %d, TypeExt: %d, BitLength: %d, Voltage: %.6f, BitValue: %d", data3[i].StartTime /1000000000., data3[i].type, data3[i].typeEx, data3[i].bitLength, data3[i].signalVoltage,data3[i].bitValue);
            if(i > 5) //write only first 5 results
            break; }
        }
      }
    }
  }
}
res = scopeDisconnect();
res =testWaitForScopeEvent(eScopeDisconnected, 8000);
```

## Availability

| Since Version |
|---|
