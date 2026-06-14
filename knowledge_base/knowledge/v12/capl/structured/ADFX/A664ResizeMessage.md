# A664ResizeMessage

> Category: `ADFX` | Type: `function`

## Syntax

```c
long A664ResizeMessage (a664Message aMessage, word newSize)
```

## Description

The message object’s payload area is resized to match the new payload size.

This affects the selectors Length and AfdxLength. If the current aMessage headers are valid (see AFDX packet validation rules), the corresponding header content is adapted as well (IP and UDP headers).

## Availability

| Since Version |
|---|
