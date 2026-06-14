# Iso11783OPGetAttribute

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPGetAttribute( dword ecuHandle, dword objectID, dword attributeID );
```

## Description

The function returns a value of an object attribute from the local object pool. A Get Attribute command is not sent to the Virtual Terminal. The object must exist in the object pool and support the attribute ID.

## Return Values

Integer value of the object.
If a value of 0 is returned, you can check with the function Iso11783GetLastError if the function succeeded.

## Example

```c
LONG objType;
objType = Iso11783OPGetAttribute( handle, 1000, 0 );
```

## Availability

| Since Version |
|---|
