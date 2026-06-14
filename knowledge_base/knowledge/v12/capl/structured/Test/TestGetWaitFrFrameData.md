# TestGetWaitFrFrameData

> Category: `Test` | Type: `function`

## Syntax

```c
long TestGetWaitFrFrameData (frFrame aFrame);
```

## Description

If a valid FlexRay frame is the last event that triggers a wait instruction, the frame’s content can be called up with the first function.

The second function can only be used for "joined events". The number of the "joined event" (return value of "testJoin...") is here being used as an index.

## Return Values

0: Data access successful

## Availability

| Since Version |
|---|
