# TCIL_ControlStop

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_ControlStop(); // form 1
```

## Description

Deactivates the Task Controller and stops sending cyclic messages. A Cannot Claim Address message is sent, if the NMT is activated and the message is not suppressed with the parameter option set to 1.

Removes all device descriptor object pools (DDOPs) too.

## Return Values

0: Function has been executed successfully

## Example

```c
void SetDataMaskSize(dword newSize)
{
  // data mask size can only be changed if TC is stopped
  TCIL_ControlStop(TC, 1);
  // wait until Working Sets have detected that TC is offline
  TestWaitForTimeout(3500);
  // change size and restart TC
  TCIL_SetNodeProperty(TC,"dataMaskSize", newSize);
  TCIL_ControlStart(TC);
}
```

## Availability

| Since Version |
|---|
