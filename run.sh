#!/bin/sh

rtl_433 -C customary -F json | python acurite-prom.py
