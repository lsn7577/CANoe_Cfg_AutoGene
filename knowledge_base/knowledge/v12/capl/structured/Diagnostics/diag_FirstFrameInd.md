# diag_FirstFrameInd

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void diag_FirstFrameInd(long source, long target, long length); // form 1
```

## Description

Indicates the start of a diagnostic data reception to the diagnostic layer.

This function is typically called from a transport layer callback. For example, the ISO TP protocol on CAN indicates the reception of a First Frame to the application.

In the diagnostic layer of a tester, a call to this function will stop the timer started after the request has been sent, i.e. even a very long data reception will not time out. If the tester has called testWaitForDiagResponseStart, that call will now be continued.

## Return Values

Error code

## Example

The OSEKTL API for the ISO TP on CAN implementation found in OSEK_TP.dll reports First Frames in the callback function OSEKTL_FirstFrameInd (see OSEK_TP). The arguments can simply be forwarded in this case:

```c
OSEKTL_FirstFrameIndication( long source, long target, long length)
{
diag_FirstFrameInd(source, target, length);
}
```

## Availability

| Since Version |
|---|
