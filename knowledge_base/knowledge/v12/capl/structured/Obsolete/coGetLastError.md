# coGetLastError

> Category: `Obsolete` | Type: `function`

## Syntax

```c
dword coGetLastError( char buffer[], dword bufferSize );
```

## Description

The function returns the error code and error text of the last function call.

If after a failed call a function is called successfully, then the last error is deleted.

## Return Values

Error code

## Example

```c
dword errCode[1];
char errText[100];

coODCreateFloat( 0x2000, 0x0, 0x1, 1, 2.5894, errCode );
if ( coGetLastError(errText, elcount(errText)) != 0){
  write( "Error %d occurred, ErrorText = %s", errCode[0], errText );
}
```

## Availability

| Up to Version |
|---|
