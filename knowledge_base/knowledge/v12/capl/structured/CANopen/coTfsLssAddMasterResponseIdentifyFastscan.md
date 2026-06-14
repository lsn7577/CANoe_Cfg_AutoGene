# coTfsLssAddMasterResponseIdentifyFastscan

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssAddMasterResponseIdentifyFastscan( dword idNumber, dword idNumberMask, dword bitCheck, dword bitCheckMask, dword sub, dword subMask, dword next, dword nextMask );
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
if (coTfsLssAddMasterResponseIdentifyFastscan( 0x000002, 0xFFFFFFFF, 28, 0xFFFFFFFF, 1, 0xFFFFFFFF, 1, 0xFFFFFFFF) {
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
