# GBT27930IL_OnTxMessage

> Category: `J1939` | Type: `function`

## Syntax

```c
void GBT27930IL_OnTxMessage( pg * txPG )
```

## Description

This callback function is called from the GBT27930 IL if a message was sent successfully.

## Example

```c
//report about the sending of  a CRM message (PGN = 0x100)
//with 0xAA in the first byte (BMS is recognized)
void GBT27930IL_OnTxMessage( pg * txPG )
{
  switch( txPG.PGN )

{
  case 0x600:
    if(txPG.byte(0) == 0xAA)
      writeEx(-3, 3, “CRM (BMS is recognized) is sent”);
    break;
  }
}
```

## Availability

| Since Version |
|---|
