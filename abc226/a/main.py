#!/usr/bin/env python3
from decimal import Decimal, ROUND_HALF_UP

N = input()

result = Decimal(N).quantize(Decimal("0"), rounding=ROUND_HALF_UP)
print(result)
