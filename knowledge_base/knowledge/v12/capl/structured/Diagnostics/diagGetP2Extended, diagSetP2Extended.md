# diagGetP2Extended, diagSetP2Extended

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetP2Extended (); // form 1: deprecated. Is equivalent to form 2 with source value 2.
```

## Description

Returns the P2 extended timeout from the selected source, or sets it to the specified value.

This function can only be used in combination with the CAPL Callback Interface.In this case you can use diagSetTimeout to specify the request timeout.

When the built-in diagnostic channel is used, the function diagSetP2Timeouts must be used to set P2 and P2-extended together.

## Parameters

| Name | Description |
|---|---|
| -1 | Deactivates "Response Pending" handling |
| 0 | Resets P2ex to its preset value |
| >0 | Sets P2ex to the value (in ms) |

## Return Values

Error code or time in ms for DiagGetP2Extended.

## Example

```c
diagSetTarget( "ECU1");
write( "Current P2 = %d", diagGetP2Timeout(0));
write( "Original value at interface = %d", diagGetP2Timeout(1));
```

## Availability

| Since Version |
|---|
