# TestWaitForFrPDU

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForFrPDU (dbFrPDU aPDU, dword aTimeout);
long TestWaitForFrPDU (char aPDUName[], dword aTimeout);
long TestWaitForFrPDU (dword aTimeout);
```

## Description

Waits for the occurrence of the specified FlexRay PDU. Should the PDU not occur before the expiration of the time aTimeout, the wait condition is resolved nevertheless.

When no PDU is specified the wait condition is resolved on any FlexRay PDU.

## Parameters

| Name | Description |
|---|---|
| aPDU | PDU to be awaited as it is defined in the database. |
| aPDUName | Name of a PDU to be awaited as it is defined in the database. |
| aTimeout | Maximum time that should be waited [ms] (Transmission of 0: no timeout controlling) |

## Example

The following test program waits for the occurrence of one of two PDUs.

It is assumed that the database defines the PDUs PDU_NMF_NODE_C and PDU_IN_CYCLE_REPETITION on the cluster FlexRay PDU.

```c
variables
{
   dword gBusContextFr;
   long resTestWaitFor, resTestGetData, resTestJoin;
   dword timeToWait  = 10; // in ms
}
void InitBusContext ()
{
   gBusContextFr = getBusNameContext("FlexRay_PDU");
   SetBusContext(gBusContextFr);
}
testcase WaitForJoinedFrPDUs_Any()
{
   FrPDU frTest;
   TestStepPass("Library: WaitForFrPDU.can", "Testcase: WaitForJoinedFrPDUs_Any");
   InitBusContext();
   // join events
   {
      TestStepPass("Call TFS function", "TestJoinFrPDUEvent(name=PDU_IN_CYCLE_REPETITION)");
      resTestJoin = TestJoinFrPDUEvent(PDU_IN_CYCLE_REPETITION);
      if (resTestJoin <= 0)
      {
         TestStepFail("Join condition", "resTestJoin = %d, Failure on joining symbolic event", resTestJoin);
         return;
      }
      else
      {
         TestStepPass("Join condition", "Joining symbolic event ok. Event number = %d", resTestJoin);
      }
      TestStepPass("Call TFS function", "TestJoinFrPDUEvent(name=PDU_NMF_NODE_C)");
      resTestJoin = TestJoinFrPDUEvent(PDU_NMF_NODE_C);
      if (resTestJoin <= 0)
      {
         TestStepFail("Join condition", "resTestJoin = %d, Failure on joining raw event", resTestJoin);
         return;
      }
      else
      {
         TestStepPass("Join condition", "Joining raw event ok. Event number = %d", resTestJoin);
      }
   }
   // wait for all events
   TestStepPass("Call TFS function", "TestWaitForAnyJoinedEvent(timeout=%d)", timeToWait);
   resTestWaitFor = TestWaitForAnyJoinedEvent(timeToWait);
   if (resTestWaitFor > 0) // Resume due to event occurred
   {
      TestStepPass("Wait condition", "Waiting for any event is ok. Resume event number = %d", resTestWaitFor);
      TestStepPass("Call TFS function", "TestGetWaitFrPDUData(index=%d)", resTestWaitFor);
      
      // extract resume event's data
      resTestGetData = TestGetWaitFrPDUData(resTestWaitFor, frTest);
      if (0 != resTestGetData)
      {
         TestStepFail("Data extraction", "resTestGetData = %d, Data access to data of event %d could not be executed!", resTestGetData, resTestWaitFor);
      }
      else
      {
         TestStepPass("Data extraction", "Data of event %d successfully extracted. SlotId=%d", resTestWaitFor, frTest.FR_SlotID);
      }
   }
   else
   {
      TestStepFail("Wait condition", "resTestWaitFor = %d, Waiting for any of joined events failed!", resTestWaitFor);
   }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.0 SP4 | 13.0 | — | — | 1.0 |
| Restricted To | — | FlexRay | FlexRay | — | — | FlexRay |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
