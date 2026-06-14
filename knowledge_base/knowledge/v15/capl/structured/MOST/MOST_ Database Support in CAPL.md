# MOST: Database Support in CAPL

> Category: `MOST` | Type: `notes`

## Description

Symbols from MOST function catalogs can be used in CAPL. The most common applications are outlined on this page.

mostAmsMessage AudioDiskPlayer.TrackPosition.Get msg;output(msg);

on mostAmsMessage AudioDiskPlayer.TrackPosition.Status{ ...}

mostAmsMessage AudioDiskPlayer.TrackPosition.Status msg;msg.Track = 5;

mostAmsMessage AudioDiskPlayer.MediaInfo.Status msg;mostParamSetString(msg, “Data.Record[].MediaTitle", idx, “Rolling Stones”);mostParamSet(msg, “Data.Record[].LastTrack", idx, 10);

Since the message data is dynamic, the parameter address ("Data.Record[].MediaTitle") cannot be checked until runtime.

mostAmsMessage AudioDiskPlayer.Random.Status msg;msg.RandomState = AudioDiskPlayer.Random.Status.RandomState::Off;

if(1 == TestWaitForMostAMSMessage("AudioDiskPlayer.TrackPosition.Status(5)", 1, 200))TestStepPass(“1”, “TrackPosition=5 reported”);

mostMsgSet(msg, "AudioDiskPlayer.SourceActivity.StartResult(1,On)", 1);ormostAmsOutput(1, "AudioDiskPlayer.SourceActivity.StartResult(1,On)", 1);

General Tips on XML Function Catalog Support in CAPL | Input Assistant | MOST: Symbolic Identification of Messages | MOST: Symbolic Identification of Parameters | Selectors

| Version 15© Vector Informatik GmbH |
|---|
