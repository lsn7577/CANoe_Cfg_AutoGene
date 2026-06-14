# coTfsEmcySendMessage

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsEmcySendMessage( dword nodeID, dword emcyCode, dword errorReg, byte inMsCodeBuf[5], dword msCodeBufSize );
```

## Description

This function sends out an emergency message.

## Return Values

Error code

## Example

```c
byte pMsCode[5] = {0,0,0,0,0};
if (coTfsEmcySendMessage(112, 0x8220, 0x20, pMsCode, 5) != 1) {
  write("coTfsSendEmcyMessage failed");
}
```
