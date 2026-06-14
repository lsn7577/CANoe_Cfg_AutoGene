# J1939ILOnRxMessage

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939ILOnRxMessage( pg * rxPG )
```

## Description

This callback function is called from the J1939 IL if the J1939 IL receives the parameter group, namely before the parameter group is processed by the J1939 IL. The message data can be manipulated in the callback method or handling of the message by the IL can be suppressed.

Usage

## Example

The following example blocks the RQST of the pgn = 0x5** (case 5) and replace the RQST of the pgn = 0x3** by the RQST of the pgn = 0x4** (case 3).

```c
long J1939ILOnRxMessage( pg * rxPG )
{
  if(rxPG.PGN == 0xEA00)
  {
    switch(rxPG.BYTE(1))
    {
    case 3:
      rxPG.BYTE(1) = 4;
      return 1;

    case 5:
      return 0;

    default:
      return 1;
    }
  }
  return 1;
}
```

## Availability

| Since Version |
|---|
