# linGetRespError

> Category: `LIN` | Type: `function`

## Syntax

```c
long linGetRespError()
```

## Description

With this function it’s possible to query the response error flag of the calling Slave node or of the Slave node specified by its node address (NAD) as last seen on the LIN bus.

## Return Values

Returns one if the queried response_error flag is set, zero if it is not set and -1 if it has not been sent yet.

## Availability

| Since Version |
|---|
