# coTfsLssWaitForSwitchStateModeGlobalRequest

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssWaitForSwitchStateModeGlobalRequest( byte[] pMode );
```

## Description

This function waits for a LSS switch state global mode request.

## Return Values

Error code

## Example

```c
byte pMode[1];

/* waits for LSS switch state global request */
if (coTfsLssWaitForSwitchStateModeGlobalRequest() == 1) {
  /* received LSS switch state global request */
  /* value in pMode[0] */
}
```
