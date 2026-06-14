# FSIL_GetLastErrorText

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long FSIL_GetLastErrorText( dword bufferSize, char buffer[] ); // form 1
```

## Description

Returns the textual description of the value of the last called FS IL function.

Returns the result of the last FS IL function as string.

Form 2 applicable in test module / test unit only.

## Return Values

0: Property has been set successfully

## Availability

| Since Version |
|---|
