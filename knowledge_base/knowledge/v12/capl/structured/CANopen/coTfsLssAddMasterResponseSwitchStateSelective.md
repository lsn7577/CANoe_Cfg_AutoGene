# coTfsLssAddMasterResponseSwitchStateSelective

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssAddMasterResponseSwitchStateSelective( dword vendorId, dword vendorIdMask, dword productCode, dword productCodeMask, dword revNo, dword revNoMask, dword serialNo, dword serialNoMask );
```

## Description

This function adds a single LSS Master request wait condition to the internal list of LSS Master request wait conditions and sends a response if a request is received.

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
if (coTfsLssAddMasterResponseSwitchStateSelective( 0x12341234, 0xFFFFFFFF, 0, 0, 0x0001, 0xFFFFFFFF, 0, 0 ) {
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
