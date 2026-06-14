# TCIL_OnRxMessage

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_OnRxMessage( pg * rxPG );
```

## Description

This callback function is called from the TC IL if the TC IL receives the parameter group, namely before the parameter group is processed by the TC IL. The message data can be manipulated in the callback method or handling of the message by the IL can be suppressed.

Usage

## Return Values

0: Received parameter group will be ignored by the TC IL

## Example

The following example blocks the RQST of the pgn = 0x5** (case 5) and replace the RQST of the pgn = 0x3** by the RQST of the pgn = 0x4** (case 3).

```c
long TCIL_OnRxMessage( pg * rxPG )
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
