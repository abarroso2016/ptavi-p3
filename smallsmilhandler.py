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
        self.idd = ""
        self.top = ""
        self.bottom = ""
        self.left = ""
        self.right = ""
        self.src = ""
        self.begin = ""
        self.dur = ""
        
        
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
        if name == 'region':
            lis.append(name)
            self.idd = attrs.get('id', "")
            SmallSMILHandler.get_tags(self,self.idd,"id")
            self.top = attrs.get('top', "")
            SmallSMILHandler.get_tags(self,self.top,"top")
            self.bottom = attrs.get('bottom', "")
            SmallSMILHandler.get_tags(self,self.bottom,"bottom")
            self.left = attrs.get('left', "")
            SmallSMILHandler.get_tags(self,self.left,"left")
            self.right = attrs.get('right', "")
            SmallSMILHandler.get_tags(self,self.right,"right")
        elif name == 'img':
            lis.append(name)
            self.src = attrs.get('src', "")
            SmallSMILHandler.get_tags(self,self.src,"src")
            self.region = attrs.get('region', "")
            SmallSMILHandler.get_tags(self,self.region,"region")
            self.begin = attrs.get('begin', "")
            SmallSMILHandler.get_tags(self,self.begin,"begin")
            self.dur = attrs.get('dur', "")
            SmallSMILHandler.get_tags(self,self.dur,"dur")
        elif name == 'audio':
            lis.append(name)
            self.src = attrs.get('src', "")
            SmallSMILHandler.get_tags(self,self.src,"src")
            self.begin = attrs.get('begin', "")
            SmallSMILHandler.get_tags(self,self.begin,"begin")
            self.dur = attrs.get('dur', "")
            SmallSMILHandler.get_tags(self,self.dur,"dur")
        elif name == 'textstream':
            lis.append(name)
            self.src = attrs.get('src', "")
            SmallSMILHandler.get_tags(self,self.src,"src")
            self.region = attrs.get('region', "")
            SmallSMILHandler.get_tags(self,self.region,"region")

smil_file = SmallSMILHandler()

if __name__ == "__main__":
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    for x in lis:
        print(x)
