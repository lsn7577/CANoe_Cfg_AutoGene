# coTfsLssClearMasterResponseList

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssClearMasterResponseList( void );
```

## Description

Clears the internal list of expected LSS Master request including the answers. The list is reset also after calling the function coTfsLssWaitForMasterRequestMessage().

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

if (coTfsLssAddMasterResponseActivateBitTiming( 1000 /*switch delay in ms*/, 0xFFFF /*switch delay bit mask*/ ) != 1) {
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
