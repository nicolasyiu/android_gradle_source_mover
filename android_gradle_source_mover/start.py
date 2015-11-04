#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import sys
import version

ACTION1 = "-replace_str"
ACTION2 = "-replace_meta"
ACTION3 = "-move_source"

#replace strings.xml key value
def replace_string(xml_path,key,new_value):
    print 'replace_string_value:'+xml_path+","+key+","+new_value

#replace metadata declare in AndroidManifest.xml
def replace_manifest_meta(xml_path,meta_name,new_value):
    print 'replace_manifest_meta:'+xml_path+","+meta_name+","+new_value

#moving sources from one to another
def move_sources(org_path,dest_path):
    print "moving sources...."

def main():
    action = sys.argv[1]

    if action == ACTION1:
        xml_path = sys.argv[2]
        key = sys.argv[3]
        new_value = sys.argv[4]
        replace_string(xml_path,key,new_value)
    elif action == ACTION2:
        xml_path = sys.argv[2]
        meta_name = sys.argv[3]
        new_value = sys.argv[4]
        replace_manifest_meta(xml_path,meta_name,new_value)
    elif action == ACTION3:
        org_path = sys.argv[2]
        dest_path = sys.argv[3]
        move_sources(org_path,dest_path)


if __name__=='__main__':
    if len(sys.argv)<=1:
        print '\nAndroid Gradle Source Mover\n'
        print 'Version:'+version.VERSION+"\n"
        print "Usage:"
        print "  "+ACTION1+"  <xml_path> <string_name> <new_value>\tReplace string value which declared in strings.xml"
        print "  "+ACTION2+" <xml_path> <meta_name> <new_value>\tReplace metadata value which declared in AndroidManifest.xml"
        print "  "+ACTION3+"  <org_path> <dest_path>\t\t\tMove sources from on place to another"
        print "\n"
    else:
        main()
