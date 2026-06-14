# Iso11783IL_OPSetStringValue

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPSetStringValue( dword objectID, char stringValue[] ); // form 1
```

## Description

The functions set the string value of an object in the object pool. The object must exist in the object pool and must support a string value. If the Object Pool API is active, a Change String Value command is sent to the Virtual Terminal. This can be suppressed with Bit 0 in options.

## Example

```c
Iso11783IL_OPSetStringValue( 1000, “Hello World” );
```

## Availability

| Since Version |
|---|
