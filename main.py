# -*- coding: utf-8 -*-
"""
@author: Utkarsh
"""

import speech_to_text as st
#import tense
while True:
    if st.convert() != -1:
        break
print("Now let's decode")