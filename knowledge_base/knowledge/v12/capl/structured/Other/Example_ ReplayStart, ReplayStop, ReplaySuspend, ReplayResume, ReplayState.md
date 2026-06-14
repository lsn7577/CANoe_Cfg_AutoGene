# Example: ReplayStart, ReplayStop, ReplaySuspend, ReplayResume, ReplayState

> Category: `Other` | Type: `notes`

## Description

variables{char replayName[32] = "ibus_data";}on key 'b'{replayStart( replayName);}on key 'e'{replayStop( replayName);}on key 's'{replaySuspend( replayName);}on key 'r'{replayResume( replayName);}on key 'w'{writeReplayState( replayName);}void writeReplayState( char name[]){switch ( replayState( name)){case 0: write( "Replay Block %s is stopped", replayName); break;case 1: write( "Replay Block %s is running", replayName); break;case 2: write( "Replay Block %s is suspended", replayName); break;default:write( "Error: Replay Block %s has an unknown state!", replayName); break;};}
