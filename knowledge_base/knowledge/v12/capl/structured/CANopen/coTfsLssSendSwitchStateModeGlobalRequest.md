# coTfsLssSendSwitchStateModeGlobalRequest

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssSendSwitchStateModeGlobalRequest( dword mode );
```

## Description

This function sends a LSS switch state global mode request.

## Return Values

Error code

## Example

```c
/* send LSS switch state global protocol request -> switch to waiting state (mode = 0) */

if (coTfsLssSendSwitchStateModeGlobalRequest( 0 ) != 1) {
  /* message could not be sent */
}
```
