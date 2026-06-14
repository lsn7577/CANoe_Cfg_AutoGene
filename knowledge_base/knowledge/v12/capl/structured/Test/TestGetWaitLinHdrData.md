# TestGetWaitLinHdrData

> Category: `Test` | Type: `function`

## Syntax

```c
long TestGetWaitLinHdrData (linheader aHeader);
```

## Description

If LIN Header event is the last event that triggers a wait instruction, the header content can be called up with the first function.The second function can only be used for "joined events". The number of the "joined event" (return value of "testJoin...") is here being used as an index.

## Return Values

0: Data access successful

## Example

```c
testcase tcTFS_linHdrEvent ()
{
   linheader  linHeaderData;
   if (testWaitForLinHeader(5000) == 1)
   {
      if (TestGetWaitLinHdrData(linHeaderData) == 0)
      {
         testStep("Evaluation", "LIN Header event occurred for FrameId=0x%X", linHeaderData.ID);
      }
   }
}
```

## Availability

| Since Version |
|---|
