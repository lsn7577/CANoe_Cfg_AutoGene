# DoIP_GetDiagnosticMessageTimeout, DoIP_SetDiagnosticMessageTimeout

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_SetDiagnosticMessageTimeout(dword toDiagnosticMessage);
```

## Description

Sets or returns the timeout waiting for a diagnostic message positive or negative acknowledgment.

## Return Values

Form 1: —Form 2: Timeout waiting for a diagnostic message positive or negative acknowledgment

## Example

This value can also be configured in the DoIP.INI file.

```c
// Expect an ACK within 1 second
DoIP_SetDiagnosticMessageTimeout(1000);
```

## Availability

| Since Version |
|---|
