#!/usr/bin/env python

import sys

import json

txt = ""


if len( sys.argv ) < 2:
	txt = sys.stdin.read()
	
else:
	with open( sys.argv[1], 'rb' ) as handle:
		txt = handle.read()


try:
	data = json.loads( txt )
except ValueError as error:
	print error
	sys.exit( 1 )


print json.dumps( data, indent = 2, sort_keys = True )
