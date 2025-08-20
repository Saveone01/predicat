import os

import numpy as np
import pandas as pd
from mymodule import alpha, zeta


def my_function(x, y, z):
    print(
        "Résultat:",
        x + y + z,
        "voilà un message incroyablement long qui devrait être coupé automatiquement par black parce qu’il dépasse largement les 88 caractères autorisés par défaut en PEP8, tu vois ?",
    )
