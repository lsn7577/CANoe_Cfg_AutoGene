# GBT27930IL_OnTxMessage

> Category: `J1939` | Type: `function`

## Syntax

```c
void GBT27930IL_OnTxMessage( pg * txPG )
```

## Description

This callback function is called from the GBT27930 IL if a message was sent successfully.

## Parameters

| Name | Description |
|---|---|
| txPG | message which was sent |

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12.0 | 13.0 | — | — | — |
| Restricted To | — | J1939 and Smart Charging | J1939 and Smart Charging | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
