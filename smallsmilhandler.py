#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


lis = []

class SmallSMILHandler(ContentHandler):
	
    def __init__ (self):
        self.width = ""
        self.height = ""
        self.background = ""
        
    def get_tags(self, valor, nombre):
        lis.append(nombre)
        lis.append(valor)
	       
    def startElement(self, name, attrs):
        if name == 'root-layout':
            lis.append(name)
            self.width = attrs.get('width', "")
            SmallSMILHandler.get_tags(self,self.width,"width")
            self.height = attrs.get('height', "")
            SmallSMILHandler.get_tags(self,self.height,"height")
            self.background = attrs.get('background-color', "")
            SmallSMILHandler.get_tags(self,self.background,"background-color")

smil_file = SmallSMILHandler()

if __name__ == "__main__":
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    for x in lis:
        print(x)
		
#region (id, top, bottom, left, right)
#img (src, region, begin, dur)
#audio (src, begin, dur)
#textstream (src, region)
