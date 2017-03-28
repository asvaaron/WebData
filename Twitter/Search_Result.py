#!/usr/bin/env pyh

class Search_Results():
        def __init__(self, user, language, body_text, site):
            self.user = user
            self.body_text = body_text
            self.site = site
            self.language = language

        def __str__(self):
            return "\n User : %s  , \n Language : %s , \n Site : %s  , \n Body text : %s " % (
            self.user.encode('utf-8'), self.language.encode('utf-8'), self.site.encode('utf-8'),
            self.body_text.encode('utf-8'))






