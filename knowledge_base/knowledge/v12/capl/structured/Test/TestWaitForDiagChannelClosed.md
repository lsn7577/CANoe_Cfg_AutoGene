# TestWaitForDiagChannelClosed

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForDiagChannelClosed(dword timeout_ms) // form 1
```

## Description

Waits for the occurrence of the state change of a diagnostic channel to the state Closed. Should the closing not occur before the expiration of the time timeout_ms, the wait condition is resolved nevertheless.

## Return Values

-2: Resume due to constraint violation

## Example

```c
if (0 == DiagCloseChannel())
{
   TestStepPass(t"Channel close called successfully");
}
else
{
   TestStepFail("Call to channel close returned an error.");
}

if (1 == TestWaitForDiagChannelClosed(1000))
{
   TestStepPass( "Channel closed successfully.");
}
else
{
   TestStepFail( "Channel could not be closed.");
}
```

## Availability

| Since Version |
|---|
