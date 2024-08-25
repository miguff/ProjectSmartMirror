#!/bin/bash
echo "Elkezdem a programot"

pm2 start run_npm.sh

echo "Várok 5 másodprecet"
sleep 20

echo "Megállítom a programot"
pm2 stop run_npm
