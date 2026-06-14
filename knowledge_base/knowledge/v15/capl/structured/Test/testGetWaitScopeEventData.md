# testGetWaitScopeEventData

> Category: `Test` | Type: `function`

## Syntax

```c
long testGetWaitScopeEventData (ScopeEvent aScopeEvent);
```

## Description

Retrieves the data of CANoe Scope event triggered by the last wait instruction.

## Parameters

| Name | Description |
|---|---|
| aScopeEvent | Data structure to be filled. |

## Example

```c
void WaitForAnyScopeEvent(enum ScopeEventType expectedEventType)
{
   long res;
   int expected;
   int received;
   ScopeEvent scopeEventData;
   if ((res = testWaitForScopeEvent(8000)) != 1)
   {
      testStepFail("","testWaitForScopeEvent (any) failed res=%d", res);
      return;
   }
   res = testGetWaitScopeEventData(scopeEventData);
   if (res != 0)
   {
      testStepFail("","testGetWaitScopeEventData failed res=%d", res);
      return;
   }
   if (scopeEventData.Type != expectedEventType)
   {
      expected = expectedEventType;
      received = scopeEventData.Type;
      testStepFail("","testGetWaitScopeEventData delivers not expected event type: expected = %d, received = %d", expected, received);
      return;
   }
   testStepPass("", "Scope event received. Data: type=%d, DataId=%d, Time=%I64d", (int)scopeEventData.Type, (int)scopeEventData.DataID, scopeEventData.Time);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.6 SP3 | 13.0 | — | — | 1.0 |
| Restricted To | — | Scope | Scope | — | — | Scope |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
