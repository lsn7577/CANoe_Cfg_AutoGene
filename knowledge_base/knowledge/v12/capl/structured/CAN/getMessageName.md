# getMessageName

> Category: `CAN` | Type: `function`

## Syntax

```c
dword getMessageName( dword id, dword context, char buffer[], dword size)
```

## Description

Finds out the message name.

## Return Values

If successful unequal 0, otherwise 0.

## Example

```c
variables
{
dword contextCAN = 0x00010000;
dword contextLIN = 0x00050000;
dword contextMOST = 0x00060000;
dword contextFLEXRAY = 0x00070000;
dword contextBEAN = 0x00080000;
dword contextJ1708 = 0x00090000;
}
on message *
{
char buffer[64];
if ( getMessageName( this.ID, contextCAN | this.CAN, buffer, elcount( buffer)))
{
write( "Message: %s", buffer);
}
}
```

## Availability

| Since Version |
|---|
