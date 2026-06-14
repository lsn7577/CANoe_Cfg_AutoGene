# beep

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void beep(int freq, int duration);
```

## Description

Tone output. In the Windows Version the parameter duration has no effect.

## Parameters

| Name | Description |
|---|---|
| freq | 0x0000 (SystemDefault) |
| freq | 0x0010 (SystemHand) |
| freq | 0x0020 (SystemQuestion) |
| freq | 0x0030 (SystemExclamation) |
| freq | 0x0040 (SystemAsterisk) |
| freq | 0xFFFF Standard Beep |

## Return Values

—

## Example

```c
void sound() {
// with sound card: 400 Hz tone / 500ms long
// without sound card: Default signal tone
beep (400,500);
}
```

## Availability

| Up to Version |
|---|
