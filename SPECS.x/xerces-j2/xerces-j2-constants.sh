#!/bin/sh
# 
# Xerces-J2 constants script
# JPackage Project (http://www.jpackage.org/)
# $Id: xerces-j2-constants.sh,v 1.3 2005/05/26 14:21:22 gbenson Exp $

# Source functions library
. /usr/share/java-utils/java-functions

# Configuration
MAIN_CLASS=org.apache.xerces.impl.Constants

# Set parameters
set_jvm
export CLASSPATH=$(build-classpath xerces-j2)
set_flags $BASE_FLAGS
set_options $BASE_OPTIONS

# Let's start
run "$@"
