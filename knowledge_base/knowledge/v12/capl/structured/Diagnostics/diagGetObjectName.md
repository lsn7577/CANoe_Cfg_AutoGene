# diagGetObjectName

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetObjectName( diagResponse obj, char nameBufferOut[], dword nameBufferLen);
```

## Description

Writes the language dependent name of the diagnostics object into the buffer. For ODX descriptions, this is the "long name".

## Return Values

Length of service name written to buffer, may be truncated.

## Example

```c
DiagRequest AirbaContr_Read req;
char name[100];
DiagGetObjectName( req, name, elcount( name));
```

## Availability

| Since Version |
|---|
