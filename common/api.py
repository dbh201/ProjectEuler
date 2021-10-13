# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 11:26:17 2021

@author: db_wi
"""

import requests
import logging

from bs4 import BeautifulSoup
      
class ProblemInfo():
    URL = "https://projecteuler.net/"
    domain = "projecteuler.net"
    path = "/"
    creds = "creds.txt"
    cache_file = "answers.txt"
    
    def __init__(self,*,cookie=None,keep_alive=None,filename=None):
        self.log = logging.getLogger(__name__)
        self.s = requests.Session()
        if not filename:
            self.filename = self.creds
        else:
            self.filename = filename
        if cookie:
            self.set_cookies(cookie,keep_alive)
        else:
            self.load_creds()
        self.cache = dict()
        self.load_cache()
    
    def load_cache(self):
        self.cache.clear()
        try:
            with open(self.cache_file,"r") as file:
                for line in file.readlines():
                    prob,ans = line.strip().split(" ")
                    self.cache[int(prob)] = int(ans)
        except FileNotFoundError:
            logging.warning("answer file not found...")
            pass
                
    def save_cache(self):
        with open(self.cache_file,"w") as file:
            for a in self.cache.keys():
                file.write(str(a) + " " + str(self.cache[a]) + '\n')
            file.truncate()
            
    def __del__(self):
        self.save_cache()
        self.save_creds()
        
    def save_creds(self):
        with open(self.filename,"w") as f:
            self.log.info("Saving creds...")
            self.log.info("%s: %s\n%s: %s" % ("PHPSESSID", self.s.cookies["PHPSESSID"],
                                              "keep_alive", self.s.cookies["keep_alive"]))
            try:
                f.write(
                    "%s\n%s\n" % (
                        self.s.cookies["PHPSESSID"],
                        self.s.cookies["keep_alive"]
                        )
                    )
            except KeyError:
                self.log.error("Couldn't save credentials - cookie invalid")
            
    def set_cookies(self,phpsessid,keep_alive=None):
        self.s.cookies.set("PHPSESSID",phpsessid,domain=self.domain,path=self.path)
        if keep_alive:
            self.s.cookies.set("keep_alive",keep_alive,domain=self.domain,path=self.path)
        
    def load_creds(self):
        with open(self.filename,"r") as f:
            self.set_cookies(f.readline().strip(),f.readline().strip())
            
    def get_answer(self,number):
        number = int(number)
        if number in self.cache:
            return self.cache[number]
        problem_str = "problem=%i" % number
        try:
            r = self.s.get(self.URL + problem_str)
        except requests.TooManyRedirects:
            self.log.error("Couldn't retrieve answer for problem %i: cookie invalid" % number)
            return None
        if r.status_code == 200:
            soup = BeautifulSoup(r.content,"html.parser")
            form = soup.find('form',{'action' : problem_str})
            if not form:
                self.log.error("Couldn't find answer form for problem %i" % number)
                self.log.error("---r.content---%s\n---------------" % r.content)
                return None
            span = form.find('span',{ 'class' : 'strong' })
            if not span:
                self.log.info("Problem %i not answered yet!" % number)
                return None
            self.cache[number] = int(span.text)
            return int(span.text)
        else:
            self.log.error("No such problem: %s" % str(number))
            return None