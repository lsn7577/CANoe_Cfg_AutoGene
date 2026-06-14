# coSetBlockSize

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coSetBlockSize( dword blockSize, dword errCode[] );
```

## Description

This function sets the block size that is used for SDO block transfers. The default value is 7 and applies globally for all SDO transmission.

## Return Values

—

## Example

```c
dword errCode[1];

coSetBlockSize( 14, errCode );
if (errCode[0] == 0) {
  write( "SDO block size successfully set" ); 
}
```

## Availability

| Up to Version |
|---|
