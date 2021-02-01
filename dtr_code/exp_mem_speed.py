
import os

for mem_budget in [6e9, 8e9, 10e9, 12e9, 14e9, 16e9]:
    os.environ['MEMORY_BUDGET'] = str(mem_budget)
    os.system('bash ./dashboard/dashboard/run_dashboard.sh dtr_home dtr_experiments')

