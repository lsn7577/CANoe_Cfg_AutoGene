# VTIL_ControlStop

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_ControlStop(); // form 1
```

## Description

Deactivates the Virtual Terminal and stops sending cyclic messages. A Cannot Claim Address message is sent, if the NMT is activated and the message is not suppressed with the parameter option set to 1.

## Return Values

0: Function has been executed successfully

## Example

```c
void SetDataMaskSize(dword newSize)
{
  // data mask size can only be changed if VT is stopped
  VTIL_ControlStop(VT, 1);
  // wait until Working Sets have detected that VT is offline
  TestWaitForTimeout(3500);
  // change size and restart VT
  VTIL_SetNodeProperty(VT,"dataMaskSize", newSize);
  VTIL_ControlStart(VT);
}
```

## Availability

| Since Version |
|---|
