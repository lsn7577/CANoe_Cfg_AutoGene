# C2xSetMapObjectText

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xSetMapObjectText( long handle, char text[] ); // form 1
```

## Description

Sets text (form 1) or formatted text (form 2) for a map object of the type text.

## Return Values

0 if success, else the set went wrong

## Example

```c
void DrawTextObject()
{
  long handle;
  float timeRemaining = 5.8;

  handle = C2xCreateMapObject( 8 );

  // set position: Motorstraße/Hemminger Straße, D-70499 Stuttgart
  C2xSetMapObjectPosition(handle, 48.825230, 9.095580);
  C2xSetMapObjectText(handle, "Traffic Light: time remaining %5.1f s", timeRemaining);
  C2xSetMapObjectFillColor(handle, makeRGB(0, 0, 0));
  C2xDrawMapObject(handle);
}
```

## Availability

| Since Version |
|---|
