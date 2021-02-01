import os

for model_name in ['tv_resnet50', 'tv_resnet152', 'tv_densenet201', 'wide_resnet101_2']:
    for mem_budget in [6e9, 8e9, 10e9, 12e9, 14e9, 16e9]:
        os.environ['DTR_MODEL_NAME'] = model_name
        os.environ['DTR_MEMORY_BUDGET'] = str(mem_budget)
        os.system('bash ./dashboard/dashboard/run_dashboard.sh dtr_home dtr_experiments')

#os.system("sudo shutdown -h now")
