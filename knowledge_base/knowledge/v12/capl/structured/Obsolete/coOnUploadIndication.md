# coOnUploadIndication

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coOnUploadIndication( dword index, dword subIndex );
```

## Description

This function is called if an SDO upload is executed on an object that was created with the access type 7. The transfer can be confirmed with coODUploadResponse or aborted with coODAbortTransfer.

The access to objects with the access type 7 is only possible with SDO expedited and SDO segmented transfer. The SDO block transfer is currently not supported for this object type.

If the SDO access is not handled by the application (CAPL), then the node layer aborts the transfer automatically after approx. 2 seconds with a SDO abort message (0x05040000 - SDO Time out).

## Return Values

—

## Example

```c
void coOnUploadIndication( dword index, dword subIndex ){
  dword errCode[1];
  byte data[4] = { 1, 2, 3, 4 };

  write( "Upload indication. [0x%.4x,0x%.2x]", index, subIndex );
  if ( index == 0x2000 ) {
    // index ok - confirm the transfer
    coODUploadResponse( 4, data, elcount(data), errCode );
  }
  else {
    // object does not exist - abort the transfer
    coODAbortTransfer( 0x06020000, errCode ); 
  }
}
```

## Availability

| Up to Version |
|---|
