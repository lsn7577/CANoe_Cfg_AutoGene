# coODUploadResponse

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coODUploadResponse( dword size, dword value, dword errCode[] );
```

## Description

The function confirms a SDO upload transfer, which was initiated on an object with access type 7. It can be used, e.g. in the event function coOnUploadIndication. If the transfer should be aborted, then coODAbortTransfer must be used.

## Return Values

—

## Example

```c
void coOnUploadIndication (dword index, dword subIndex){
  dword errCode[1]; 

  if (index == 0x2000) {
coODUploadResponse( 2, 0x1234, errCode );
    if (errCode[0] == 0) {
      write("SDO upload successfully confirmed");
    }
  }
}
```

## Availability

| Up to Version |
|---|
