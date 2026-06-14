# diagSetTimeout

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagSetTimeout (DWORD timeout)
```

## Description

Specifies the request timeout.

A diagnostics response must start within this time, i.e. this corresponds to the P2 timeout.

This function can only be used in combination with the CAPL Callback Interface.In this case you can use diagSetP2Extended to specify the handling of pending responses.

When the built-in diagnostic channel is used, the function diagSetP2Timeouts must be used to set P2 and P2-extended together.

It is recommended to define the times P2 Timeout and P2 Extended as short as possible and just as long as necessary. In particular you should mind that these times have to have a smaller value than the application timeout (VDSRequestApplicationTimeout in CAN.ini). The application timeout makes sure that waiting for a final response will be aborted if an ECU continuously responds "response pending" to a request.

## Return Values

Error code

## Availability

| Since Version |
|---|
