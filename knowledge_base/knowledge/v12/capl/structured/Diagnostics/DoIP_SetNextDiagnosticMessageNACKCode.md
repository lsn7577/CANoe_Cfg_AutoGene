# DoIP_SetNextDiagnosticMessageNACKCode

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_SetNextDiagnosticMessageNACKCode(long NACKCode);
```

## Description

Sets the next return code sent in the acknowledgment for a diagnostic message received. The code is reset to 0 (positive) after usage.

Values other than 0 let the peer assume that transmission failed, i.e. error handling is necessary by the peer.

## Return Values

—

## Example

```c
on key 'n' {
  write( “The next diagnostics message will get a negative ack”);
  DoIP_SetNextDiagnosticMessageNACKCode(3);
}
```

## Availability

| Since Version |
|---|
