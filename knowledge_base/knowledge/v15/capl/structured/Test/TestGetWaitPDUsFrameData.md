# TestGetWaitPDUsFrameData

> Category: `Test` | Type: `function`

## Syntax

```c
long TestGetWaitPDUsFrameData (message * msg); // form 1
long TestGetWaitPDUsFrameData (ethernetPacket * packet); // form 2
long TestGetWaitPDUsFrameData (FrFrame * frame); // form 3
long TestGetWaitPDUsFrameData (dword explicitJoinIndex, message * msg); // form 4
long TestGetWaitPDUsFrameData (dword explicitJoinIndex, ethernetPacket * packet); // form 5
long TestGetWaitPDUsFrameData (dword explicitJoinIndex, FrFrame * frame); // form 6
```

## Description

If a valid PDU is the last event that triggers a wait instruction, the message’s, packet’s or frame’s content that contained the PDU can be called up with form 1-3.

Form 4-6 can only be used for joined events. The number of the joined event (return value of TestJoin...) is here being used as an index.

## Parameters

| Name | Description |
|---|---|
| frame | Message variable of type CAN message, Ethernet Packet or FlexRay frame that should be filled in with this function. It has to be either a type free message variable, or a message variable that was created for the PDU type that triggered the wait instruction. |
| explicitJoinIndex | Number of the joined event corresponds with the return value of TestJoin.... |

## Example

```c
testcase Test_01()
{
  long ret;
  PDU PDU_A aPDU_01;
  message * aMsg_01;

  ret = TestWaitForPDU(dbPDU::PDU_A, 0, 250);

  if(ret != 1)
  {
    TestStepFail("Error: PDU not received");
  }
  else
  {
    ret = TestGetWaitPDUsFrameData(aMsg_01); // PDU is assumed to be sent on CAN
    if(ret != 0)
    {
      TestStepFail("Error: Can not access PDU");
    }
    else
    {
      TestStepPass("OK", "Received PDU in message with CAN ID %lu", aMsg_01.ID);
    }
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 SP3 | 13.0 | — | — | 2.1 SP3 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
