# coODDownloadResponse

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coODDownloadResponse( dword errCode[] );
```

## Description

The function confirms a SDO download transfer, which was initiated on an object with access type 7. It can be used, e.g. in the event function coOnDownloadIndication. If the transfer should be aborted, then coODAbortTransfer must be used.

## Return Values

—

## Example

```c
void coOnDownloadIndication (dword index, dword subIndex, dword size, dword dataValid){
  dword errCode[1]; 

  if (index == 0x2000) {
coODDownloadResponse( errCode );
    if(errCode[0] == 0) {
      write("SDO download successfully confirmed");
    }
  }
}
```

## Availability

| Up to Version |
|---|
