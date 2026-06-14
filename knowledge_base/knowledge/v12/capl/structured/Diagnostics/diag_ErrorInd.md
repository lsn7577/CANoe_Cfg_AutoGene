# diag_ErrorInd

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void diag_ErrorInd (long error); // form 1
```

## Description

Reports errors to the diagnostic layer.

This function is typically called within a transport layer callback. The transport layer uses it to report errors to the diagnostic layer.

If, for example, testWaitForDiagResponse is used in a test module to wait for receipt of a response and Diag_ErrorInd reports an error, the test function returns an error and stops waiting.

## Return Values

Error code

## Availability

| Since Version |
|---|
