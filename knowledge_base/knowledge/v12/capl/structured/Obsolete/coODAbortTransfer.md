# coODAbortTransfer

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coODAbortTransfer( dword abortCode, dword errCode[] );
```

## Description

The function aborts a SDO transfer, which was initiated on an object with access type 7. It can be used in the event functions coOnDownloadIndication or coOnUploadIndication.

## Return Values

—

## Example

```c
void coOnUploadIndication (dword index, dword subIndex) {
  dword errCode[1];
  if (index > 0x2003) {
coODAbortTransfer( 0x06020000, errCode ); // object doesn't exist
    if (errCode[0] == 0) {
      write( "Aborting SDO transfer successfully initiated" ); 
    }
  }
}
```

## Availability

| Up to Version |
|---|
