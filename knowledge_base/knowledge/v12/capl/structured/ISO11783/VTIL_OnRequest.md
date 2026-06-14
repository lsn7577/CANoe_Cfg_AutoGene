# VTIL_OnRequest

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_OnRequest( long rqPGN, long sourceAddr );
```

## Description

This callback function is called from the VT IL if a request (0xEA00) is received.

## Return Values

0: Do not respond to the request

## Example

```c
long VTIL_OnRequest( long rqPGN, long sourceAddr )
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
