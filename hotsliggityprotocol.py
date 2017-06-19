import os
import sys
import argparse
import json
import requests

import matchrequest
import match

mpyq_path = os.path.abspath(os.path.join('vendor\heroprotocol'))
print mpyq_path
sys.path.append(mpyq_path)

from mpyq import mpyq
import protocol29406

class EventLogger:
    def __init__(self):
        self._event_stats = {}

    def log(self, output, event):
        # Write structure

        s = json.dumps(event, encoding="ISO-8859-1");
        print(s);

if __name__ == '__main__':
    
    match = match.Match();
    
    # TODO: Pull .StormReplay files from its default install location, loop through it, & read in all *.StormReplay files

    # Set up an args parser to accept .StormReplay file
    parser = argparse.ArgumentParser()
    parser.add_argument('replay_file', help='.StormReplay file to load')

    args = parser.parse_args()

    archive = mpyq.MPQArchive(args.replay_file)

    logger = EventLogger()

    # Read the protocol header, this can be read with any protocol
    contents = archive.header['user_data_header']['content']
    header = protocol29406.decode_replay_header(contents)

    baseBuild = header['m_version']['m_baseBuild']

    try:
        protocol = __import__('protocol%s' % (baseBuild,))
    except:
        print >> sys.stderr, 'Unsupported base build: %d' % baseBuild
        sys.exit(1)

    # Get protocol details
    contents = archive.read_file('replay.details')
    details = protocol.decode_replay_details(contents)
    playerList = details['m_playerList']
    for playerName in playerList:
        if playerName['m_name'] == "Funda":
            hero = playerName['m_hero'];
            match.setHeroName(hero);
            logger.log(sys.stdout, match.__dict__)

    # TODO: Add other decoders to complete matchRequest before posting

    # Point to HotSliggityService locally
    url = 'http://localhost:8080/test'

    matchRequest = matchrequest.MatchRequest();

    matchRequest.matches[0] = match.__dict__;

    # TODO: Figure out correct format for "data" attribute of post method below
    requests.post(url, data=matchRequest);