# AFDX Copy-Operator

> Category: `ADFX` | Type: `function`

## Syntax

```c
target-object = source-object
```

## Description

The copy-operator allows to copy the following object combinations:

1. A664Message on A664Message

2. A664Message on A664Frame

3. A664Frame on A664Frame.

It is explicitly not allowed to copy a A664Frame on to a A664Message (as this might violate the A664Message integrity).

## Example

```c
a664Message DEMOMSG_ALLTYPES myMsg = { msgChannel = 1};
a664Message * myMsg2;
a664Frame *     myFrame;

myMsg2 = myMsg;		// copy myMsg onto myMsg2
//myMsg2.EthVlId = 2;	// forbidden for messages


write("Msg2 as copy from Msg: #Ch:%d VlId=%x name:=%s",
myMsg2.msgChannel,
myMsg2.EthVlId, myMsg2.name);

myFrame = myMsg;		// copy myMsg onto myFrame
myFrame.EthVlId = 1;	// allowed for frames

write("myFrame as copy from Msg: #Ch:%d VlId=%x name:=%s", myFrame.msgChannel,

myFrame.EthVlId, myFrame.name);
myFrame.EthVlId = 3;
myFrame.msgChannel = 2;

write("myFrame modified2: #Ch:%d VlId=%x name:=%s", myFrame.msgChannel,
myFrame.EthVlId, myFrame.name);
```
