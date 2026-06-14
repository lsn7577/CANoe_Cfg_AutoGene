# coTfsLssSendSwitchStateSelectiveSequence

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssSendSwitchStateSelectiveSequence( dword vendorId, dword productCode, dword revisionNo, dword serialNo );
```

## Description

The function sends a switch state selective messages and waits for the response.

## Return Values

Error code

## Example

```c
/* send LSS switch state selective protocol request */

if (coTfsLssSendSwitchStateSelectiveSequence( 0x12345678,  0x11223344, 0x87654321, 0x1) != 1) {
  /* message could not be sent */
}
```
