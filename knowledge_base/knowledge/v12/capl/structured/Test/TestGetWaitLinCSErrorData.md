# TestGetWaitLinCSErrorData

> Category: `Test` | Type: `function`

## Syntax

```c
long TestGetWaitLinCSErrorData (linCSError apEvent);
```

## Description

Retrieves the data of a checksum error triggered by the last wait instruction.The second function can only be used for "joined events". The number of the "joined event" (return value of "testJoin...") is here being used as an index.

## Return Values

0: Data access was successful

## Example

```c
testcase tcTFS_linCSError ()
{
   linCSError linCSErrorData;
   if (testWaitForLinCSError(5000) == 1)
   {
      if (testGetWaitLinCSErrorData(linCSErrorData) == 0)
      {
         testStep("Evaluation", "LIN CS Error event occurred for FrameId=0x%X", linCSErrorData.ID);
      }
   }
}
```

## Availability

| Since Version |
|---|
