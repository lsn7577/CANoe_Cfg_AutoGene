# Iso11783IL_OnRxMessage

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OnRxMessage( pg * rxPG );
```

## Description

This callback function is called from the Iso11783 IL if the Iso11783 IL receives the parameter group, namely before the parameter group is processed by the Iso11783 IL. The message data can be manipulated in the callback method or handling of the message by the IL can be suppressed.

Usage

## Return Values

0: Received parameter group will be ignored by the ISO11783 Interaction Layer

## Example

The following example ignores messages from a Virtual Terminal e.g. to communicate with a second Virtual Terminal.

```c
LONG Iso11783IL_OnRxMessage ( pg * rxPG )
{
  if( (rxPG.PGN == VT12_VT.pgn) && (txPG.sa == 38))
    return 0;
  return 1;
}
The following example blocks the RQST of the pgn = 0x5** (case 5) and replace the RQST of the pgn = 0x3** by the RQST of the pgn = 0x4** (case 3)
long Iso11783IL_OnRxMessage( pg * rxPG )
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
