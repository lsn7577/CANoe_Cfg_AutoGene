# diag_RequestDone

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diag_RequestDone(); // form 1
```

## Description

The processing of the current diagnostic request completed. This function can be called if the diagnostic communication layer detected a timeout, i.e. the ECU did not respond in time. Calling this function allows the CAPL program to abort waiting for a response on the request.

## Return Values

Error code

## Example

```c
on timer tP2
{
  // No response was received within P2
  diag_RequestDone( gCurrentECU);
}
```

## Availability

| Since Version |
|---|
