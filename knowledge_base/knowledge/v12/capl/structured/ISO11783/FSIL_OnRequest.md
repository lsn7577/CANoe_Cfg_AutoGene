# FSIL_OnRequest

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long FSIL_OnRequest( long rqPGN, long sourceAddr );
```

## Description

Is called if a request (0xEA00) is received.

The return value defines the node reaction to the request.

## Return Values

0: Do not respond to the request

## Example

```c
long FSIL_OnRequest( long rqPGN, long sourceAddr )
{
  switch( rqPGN ) {
  case 0xFF02:
    return 2; // send NACK
  }
  return 1;
}
```

## Availability

| Since Version |
|---|
