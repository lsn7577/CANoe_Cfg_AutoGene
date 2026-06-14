# J1939ILOnRequest

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939ILOnRequest( long rqPGN, long sourceAddr )
```

## Description

This callback function is called from the J1939 IL if a request (0xEA00) is received.

## Example

```c
LONG J1939ILOnRequest( LONG rqPGN, LONG sourceAddr )
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
