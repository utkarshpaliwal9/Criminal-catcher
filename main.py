# -*- coding: utf-8 -*-
"""
@author: Utkarsh
"""

import speech_to_text as st
import tense


while True:
    sent = st.convert()
    if sent != -1:
        break
print("Now let's decode")
info = tense.getInfo(sent)
print(*info)
print(sent)