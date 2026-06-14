# diagSetP2Timeouts

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagSetP2Timeouts( dword newP2timeout_ms, dword newP2exTimeout_ms); // form 1
```

## Description

Changes the P2 and P2ex timeout values at the built-in diagnostic channel.

Use this function only for the built-in diagnostic channel. In combination with the CAPL Callback Interface use diagSetTimeout.

It is recommended to define the times P2 Timeout and P2 Extended as short as possible and just as long as necessary. In particular you should mind that these times have to have a smaller value than the application timeout (VDSRequestApplicationTimeout in CAN.ini). The application timeout makes sure that waiting for a final response will be aborted if an ECU continuously responds "response pending" to a request.

## Return Values

-1 for failed or error code.

## Availability

| Since Version |
|---|
