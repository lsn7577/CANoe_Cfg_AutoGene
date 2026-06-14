# SetMediaFile

> Category: `Other` | Type: `function`

## Syntax

```c
SetMediaFile(panel, control, mediafile);
```

## Description

Replaces the media file of the Panel Designer Media Player control during runtime.

The panel is accessed by its individual panel name that is entered in the Panel Designer.

## Return Values

—

## Example

Setting media file using absolute path.

Setting media file using relative path. The media file is in the Videos folder and this folder is parallel to the panel folder.

```c
on key 'x'
{
SetMediaFile("Movie", "Media Player", "D:\\Example\\MediaPlayerProject\\Videos\\song.mpg");
}
on key 'y'
{
SetMediaFile("Movie", "Media Player", "..\\Videos\\song.mpg");
}
```

## Availability

| Since Version |
|---|
