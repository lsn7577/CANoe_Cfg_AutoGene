# FSIL_ControlStop

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long FSIL_ControlStop(); // form 1
```

## Description

Deactivates the File Server and stops sending cyclic messages.

A Cannot Claim Address message is sent, if the NMT is activated and the message is not suppressed with the parameter option set to 1.

Removes all device descriptor object pools (DDOPs) too.

## Return Values

0: Function has been executed successfully

## Example

```c
void SetDataMaskSize(dword newSize)
{
  // data mask size can only be changed if FS is stopped
  FSIL_ControlStop(FS, 1);
  // wait until Working Sets have detected that FS is offline
  TestWaitForTimeout(3500);
  // change size and restart FS
  FSIL_SetNodeProperty(FS,"dataMaskSize", newSize);
  FSIL_ControlStart(FS);
}
```

## Availability

| Since Version |
|---|
