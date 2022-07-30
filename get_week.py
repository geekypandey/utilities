#!/bin/env python
# Get Current Week from Saturday to next Friday

import sys
from datetime import datetime, timedelta

if len(sys.argv) < 2:
    print("Provide the Week No.")
    sys.exit(1)

week_no = sys.argv[1]

today = datetime.today()
weekday = today.weekday()
diff = abs(weekday - 5)

start_date = today - timedelta(days=diff)
end_date = start_date + timedelta(days=6)

result = f'Week {week_no} ({start_date.strftime("%d/%m/%Y")} - {end_date.strftime("%d/%m/%Y")})'
print(result)
