#!/bin/bash

./sendcommand.py "shutdown(auth_type=admin,auth_name=system,auth_pass=test,auth_remoteaddr=1.1.1.1)"
sleep 3
../start.py

