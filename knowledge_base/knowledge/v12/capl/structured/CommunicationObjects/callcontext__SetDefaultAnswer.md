# callcontext::SetDefaultAnswer

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
void callContext::SetDefaultAnswer()
```

## Description

Sets the return value and the out parameters for the call to their defaults.

The values are set to their defaults on receival of a call if the AutoAnswerMode is set to Auto. You can (re)set them explicitly with this method.

You can change the defaults with the ParamDefaults and DefaultResult properties at the provider endpoint.

## Return Values

—

## Example

```c
on fctCalled MirrorAdjustment.providerSide[all,LeftMirror].Adjust
{
  this.SetDefaultAnswer();
  this.SetTimeToAnswer(10);
}
```

## Availability

| Since Version |
|---|
