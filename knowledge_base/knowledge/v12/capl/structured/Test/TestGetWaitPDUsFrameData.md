# TestGetWaitPDUsFrameData

> Category: `Test` | Type: `function`

## Syntax

```c
long TestGetWaitPDUsFrameData (message * msg); // form 1
```

## Description

If a valid PDU is the last event that triggers a wait instruction, the message’s, packet’s or frame’s content that contained the PDU can be called up with form 1-3.

Form 4-6 can only be used for joined events. The number of the joined event (return value of TestJoin...) is here being used as an index.

## Return Values

0: Data access successful.

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

| Since Version |
|---|
