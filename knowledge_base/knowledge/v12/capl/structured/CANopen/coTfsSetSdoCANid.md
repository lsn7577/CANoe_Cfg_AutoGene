# coTfsSetSdoCANid

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSetSdoCANid( dword sdoClnRxId, dword sdoClnTxId );
```

## Description

With this function the internal the CAN identifiers to be used for the SDO tests are set. All test functions, which uses SDO access, will use the specified identifiers. This setting will override the application profile specific SDO id settings.

## Return Values

Error code

## Example

```c
coTfsSetSdoCANid(0x580, 0x602); // set internal CAN-ID for Rx SDOs to 0x580 and for Tx SDOs to 0x602
```
