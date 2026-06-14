# SetVideoOfflineSource

> Category: `Other` | Type: `function`

## Syntax

```c
SetVideoOfflineSource(char windowName[], long sourceType, char sourcePath[]);
```

## Description

Sets the offline source (type and path) for a CANoe Video Window.

## Return Values

—

## Example

```c
on preStart
{
  //Configure offline source (video file)
  SetVideoOfflineSource("Video Window", 1, "MyVideoFile.avi");
}
```

## Availability

| Since Version |
|---|
