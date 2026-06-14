# TCIL_SetNodeProperty

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_SetNodeProperty( char propertyName[], long propertyValue); // form 1
```

## Description

Changes an internal property of the node.

## Return Values

0: Property has been set successfully

## Example

```c
void SetLanguageToEnglish()
{
  TCIL_SetNodeProperty(TC, "languageCode", 0x656E); // 'en'
}
```

## Availability

| Since Version |
|---|
