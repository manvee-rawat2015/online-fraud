# -*- coding: utf-8 -*-
"""finalpractical.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12tE4aluD7HjAEmLk79b0I8yLf1RMxe04
"""

import sys
print(sys.version)

!pip install streamlit -q

!wget -q -O - ipv4.canhazip.com

!npm install -g localtunnel
!streamlit run picklefile.py & npx localtunnel --port 8501