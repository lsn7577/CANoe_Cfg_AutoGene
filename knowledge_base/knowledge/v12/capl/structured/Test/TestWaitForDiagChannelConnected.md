# TestWaitForDiagChannelConnected

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForDiagChannelConnected(dword timeout_ms); // form 1
```

## Description

Waits for the occurrence of the state change of a diagnostic channel to the state Connected. Should the connection not occur before the expiration of the time timeout_ms, the wait condition is resolved nevertheless.

## Return Values

-2: Resume due to constraint violation

## Example

```c
long status;
   if (0 == DiagConnectChannel())
   {
      TestStepPass( "Channel connect called successfully.");
   }
   else
   {
      TestStepFail( "Channel connect returned with an error.");
      success = kRetFail;
   }

status = TestWaitForDiagChannelConnected(2000);
   if (1 == status)
   {
      TestStepPass("Connected to target ECU");
   }
   else
   {
      TestStepFail( "Error connecting to target ECU");
   }
```

## Availability

| Since Version |
|---|
