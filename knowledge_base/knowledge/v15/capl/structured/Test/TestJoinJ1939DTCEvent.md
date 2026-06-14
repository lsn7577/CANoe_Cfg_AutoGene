# TestJoinJ1939DTCEvent

> Category: `Test` | Type: `function`

## Syntax

```c
long TestJoinJ1939DTCEvent (dword sourceAddress, Message message, dword spn); // form 1
long TestJoinJ1939DTCEvent (dword sourceAddress, dword pgn, dword spn); // form 2
long TestJoinJ1939DTCEvent (Node node, Message message, dword spn); // form 3
long TestJoinJ1939DTCEvent (Node node, dword pgn, dword spn); // form 4
long TestJoinJ1939DTCEvent (dword sourceAddress, Message message, dword spn, word fmi, word oc); // form 5
long TestJoinJ1939DTCEvent (dword sourceAddress, dword pgn, dword spn, word fmi, word oc); // form 6
long TestJoinJ1939DTCEvent (Node node, Message message, dword spn, word fmi, word oc); // form 7
long TestJoinJ1939DTCEvent (Node node, dword pgn, dword spn, word fmi, word oc); // form 8
```

## Description

Completes the current set of joined events with the additional Diagnostic Trouble Code (DTC) event – transmitted with one of the J1939 diagnostic messages. This function does not wait.

The affected message (specified by the Parameter Group number pgn or the database object message) must be able to contain a DTC, so only this parameter groups are allowed: DM1, DM2, DM4, DM6, DM12, DM23, DM24, DM27, DM28, DM31, DM35 and DM41-DM54.

## Parameters

| Name | Description |
|---|---|
| message | Message containing the specified DTC. Must be a J1939 Parameter Group. |
| pgn | Parameter Group Number (with data page) of the message containing the specified DTC. |
| node | Sender of the message containing the specified DTC. |
| sourceAddress | Source address of the message containing the specified DTC 0xFFFFFFFF if source address is to be ignored. |
| spn | Suspect Parameter Number of the specified DTC 0xFFFFFFFF if spn is to be ignored. |
| fmi | Failure Mode Identifier of the specified DTC 0xFFFF if fmi is to be ignored. |
| oc | Occurrence Counter of the specified DTC 0xFFFF if oc is to be ignored. |

## Example

```c
testcase tcWaitForOneOfDTCs(dword sourceAddress)
{
  long eventIndex;
  dword sa = 0x1;

  //All DTCs are transmitted with the message DM12 (pgn = 0xFED4).
  dword pgnDM12 = 0xFED4;

  //DTC Condition 1: spn = 111, fmi = 12, oc to be ignored
  TestJoinJ1939DTCEvent (sourceAddress, pgnDM12, 111, 12, 0xFFFF);

  //DTC Condition 2: spn = 222, fmi to be ignored, oc = 5
  TestJoinJ1939DTCEvent (sourceAddress, pgnDM12, 222, 0xFFFF, 5);

  //DTC Condition 3: spn = 333, fmi and oc to be ignored
  TestJoinJ1939DTCEvent (sourceAddress, pgnDM12, 333, 0xFFFF, 0xFFFF);

  eventIndex = testWaitForAnyJoinedEvent(5000);
  switch (eventIndex)
  {

    case 1:
      testStepPass("Validation", "DTC with spn=111 and fmi=12 occurred");
      break;

    case 2:
      testStepPass("Validation", "DTC with spn=222 and oc=5 occurred");
      break;

    case 3:
      testStepPass("Validation", "DTC with spn=333 occurred");
      break;

    default:
      testStepFail("Validation", "Unexpected event or timeout (return code %d)", eventIndex);
      break;

  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.5: forms 1, 2, 3, 4 12.0: forms 5, 6, 7, 8 | 13.0 | — | — | 2.0: forms 1, 2, 3, 4 4.0: forms 5, 6, 7, 8 |
| Restricted To | — | J1939 | J1939 | — | — | J1939 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
