# TestGetWaitFrPDUData

> Category: `Test` | Type: `function`

## Syntax

```c
long TestGetWaitFrPDUData (frPDU aPDU);
```

## Description

If a valid FlexRay PDU is the last event that triggers a wait instruction, the PDU’s content can be called up with the first function.

The second function can only be used for "joined events". The number of the "joined event" (return value of "testJoin...") is here being used as an index.

## Return Values

0: Data access successful

## Availability

| Since Version |
|---|
