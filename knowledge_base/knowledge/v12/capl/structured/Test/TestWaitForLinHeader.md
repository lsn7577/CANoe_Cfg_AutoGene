# TestWaitForLinHeader

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForLinHeader (dbMessage aFrame, dword aTimeout);
```

## Description

Waits for the Header occurrence of the specified LIN frame. Should the header not occur before the expiration of the time aTimeout, the wait condition is resolved nevertheless.

When no frame is specified the wait condition is resolved on any LIN header.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Return Values

-2: Resume due to constraint violation

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
