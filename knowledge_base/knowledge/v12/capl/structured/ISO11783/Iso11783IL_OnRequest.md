# Iso11783IL_OnRequest

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OnRequest( long rqPGN, long sourceAddr );
```

## Description

This callback function is called from the ISO11783 IL if a request (0xEA00) is received.

## Return Values

0: Do not respond to the request

## Example

```c
LONG Iso11783IL_OnRequest( LONG rqPGN, LONG sourceAddr )
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
