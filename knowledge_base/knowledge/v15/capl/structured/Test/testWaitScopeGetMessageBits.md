# testWaitScopeGetMessageBits

> Category: `Test` | Type: `function`

## Syntax

```c
long testWaitScopeGetMessageBits(message msg, ScopeAnalysisSetup setup, dword arraySize, scopeBitData signalData1[], scopeBitData signalData2[], scopeBitData signalData3[]);
```

## Description

A CAN message stored in the scope buffer will be parsed. For each bit of the message the signal voltage levels, the bit length, and the bit type will be returned.

## Parameters

| Name | Type | Description |
|---|---|---|
| msg |  | The message the bits are fetched. |
| Keyword | Description | Type |
| samplePoint | Sample point in percent. At this point the signal level will be measured. Classic CAN: Value will be used for all bits of the message. CAN FD: Value will be used for the bits of the arbitration phase. | char |
| samplePointDataPhase | Sample point in percent. At this point the signal level will be measured.Classic CAN: Value will not be used.CAN FD: Value will be used for the bits of the data phase. | char |
| arraySize |  | [in] the size of the arrays signalData1, signalData2, and signalData3 [out] the number of bits parsed and stored in the signalData-arrays. |
| Keyword | Description | Type |
| type | Type of the bit, see ScopeBitAnalyse.cin | word |
| typeEx | 0: data bit, 1: stuff bit | word |
| bitValue | Logical bit value (0, or 1) | byte |
| startTime | Time stamp of bit start in ns | qword |
| bitLength | Length of the bit in ns | long |
| signalVoltage | Signal voltage at the sampling point | float |
| signalPolarity | Signal polarity:0 = CAN high - CAN low1 = CAN low - CAN high | byte |

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 SP2 | 13.0 | — | — | 1.1 SP2 |
| Restricted To | — | CAN Scope | CAN Scope | — | — | Scope |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
