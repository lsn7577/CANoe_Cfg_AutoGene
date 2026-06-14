# mostSetRetryParameter, mostGetRetryParameter

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostSetRetryParameter(long channel, long id, long value)
```

## Description

The functions provide access to the transceiver chip parameters for message transmission. The number of low-level transmission attempts and delay between attempts can be set and retrieved.

## Return Values

mostSetRetryParameter: See error codes.

## Example

```c
// configure MOST transceiver for 5 low-level transmission attempts on Control channel
mostSetRetryParameter(1, 0, 5);
```

## Availability

| Since Version |
|---|
