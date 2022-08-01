import os 
for i in range(3):
    os.system('CUDA_VISIBLE_DEVICES=3 python3 src/main.py --config=dmix --env-config=pred_prey_punish with t_max=1000000 local_results_path=./results/pred/dmix_s2n_500000 risk_start=1.0 risk_finish=0.0 test_lower_risk=0.0 test_upper_risk=1.0 risk_anneal_time=500000')