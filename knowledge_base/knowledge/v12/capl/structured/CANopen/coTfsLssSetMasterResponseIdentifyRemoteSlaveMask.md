# coTfsLssSetMasterResponseIdentifyRemoteSlaveMask

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssSetMasterResponseIdentifyRemoteSlaveMask( dword vendorIdMask, dword productCodeMask, dword revisionNoLowMask, dword revisionNoHighMask, dword serialNoLowMask, dword serialNoHighMask );
```

## Description

This function sets the masks for the parameters of function coTfsLssAddMasterResponseIdentifyRemoteSlave and has to be called before that function.

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

if (coTfsLssSetMasterResponseIdentifyRemoteSlaveMask( 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF ) {
  if (coTfsLssAddMasterResponseIdentifyRemoteSlave( 0x1234, 0x43214321, 0, 0xFFFFFFFF, 0, 1000 ) {
    write("could not add request");
    return;
  }
}

/* wait for any of the events configured before */
if (coTfsLssWaitForMasterRequestMessage() != 1) {
  write("no event received");
}
else {
  write("event received");
}
```
