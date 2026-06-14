# GBT27930IL_OnTxPrepare

> Category: `J1939` | Type: `function`

## Syntax

```c
long GBT27930IL_OnTxPrepare( pg * txPG )
```

## Description

This callback function is called from the GBT27930 IL before a parameter group is sent. The signal value can be updated in the callback or sending of the message can be suppressed.

## Example

```c
//Block the CRM message (PGN = 0x0100) if the first byte is 0x00
//Modify the BCL message (PGN = 0x1000):
//  switch the charging mode from "constant current" to "constant voltage"
long GBT27930IL_OnTxPrepare( pg * txPG )
{
  int retValue = 1;
  switch( txPG.PGN )
  {
    case 0x0100:
      if(txPG.byte(0) == 0x9)
        retValue = 0;
      break;
    case 0x1000:
      if(txPG.byte(4) == 0x2)
          txPG.byte(4) = 0x1;
      break;
  }
  return retValue;
}
```

## Availability

| Since Version |
|---|
