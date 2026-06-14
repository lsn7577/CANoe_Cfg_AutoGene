# coTfsLssAddMasterResponseSwitchStateGlobal

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssAddMasterResponseSwitchStateGlobal( dword mode, dword modeMask );
```

## Description

This function adds a single LSS Master request wait condition to the internal list of LSS Master request wait conditions.

## Return Values

Error code

## Example

```c
/* clear internal check list */
if (coTfsLssClearMasterResponseList() != 1) {
  write("Clear list failed");
  return;
} 

/* add one or more test functions */
if (coTfsLssAddMasterResponseSwitchStateGlobal( 0, 0xFFFFFFFF ) {
  write("could not add request");
  return;
} 

/* wait for any of the events configured before */
if (coTfsLssWaitForMasterRequestMessage() != 1) {
  write("no event received");
} 
else {
  write("event received");
}
```
