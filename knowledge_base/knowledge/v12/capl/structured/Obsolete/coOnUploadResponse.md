# coOnUploadResponse

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coOnUploadResponse( dword nodeId, dword index, dword subIndex, dword size );
```

## Description

This function is called when the response to an SDO upload was received (see coUpload). Now the data can be accessed with coThisGetSigned, coThisGetUnsigned, coThisGetFloat, coThisGetData, and coThisGetSize.

The access to the transmitted data is only possible within this function.

## Return Values

—

## Example

```c
void coOnUploadResponse( dword nodeId, dword index, dword subIndex, dword size ){
  dword errCode[1];
  dword value;
  value = coThisGetUnsigned( errCode );
  write( "Upload Response Data 0x%X", value );
}
```

## Availability

| Up to Version |
|---|
