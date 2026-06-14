# TestWaitForLinCSError

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForLinCSError(dword aTimeout);
```

## Description

Waits for a checksum error for the specified amount of time.

Consider to set always the appropriate bus context in a multibus environment before the function is called.

Further information on site MultiBus Environment.

## Return Values

-2: Resume due to constraint violation

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
