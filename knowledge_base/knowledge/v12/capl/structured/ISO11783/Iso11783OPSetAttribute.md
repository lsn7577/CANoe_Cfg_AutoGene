# Iso11783OPSetAttribute

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPSetAttribute( dword ecuHandle, dword objectID, dword attributeID, long value );
```

## Description

The function sets an attribute value of an object. The object must exist in the object pool and support the attribute ID. If the Object Pool API is active, the Change Attribute command (175) is sent to the Virtual Terminal. This can be suppress with Bit 0 in options.

## Example

```c
Iso11783OPSetAttribute( 
 handle, 1000, 3, 20 );
```

## Availability

| Since Version |
|---|
