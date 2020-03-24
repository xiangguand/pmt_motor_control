import pickle
import matplotlib.pyplot as plt
from mypickle import save2pickle, load_pickle
import os
import numpy as np

FIG_DIR = "figure"
def plot_data(DATA_DIR, pickle_last_nm, DELTA_T):
    try:
        os.mkdir(FIG_DIR)
    except:
        pass

    i1 = load_pickle(DATA_DIR+'/i1'+pickle_last_nm+'.pickle')
    i2 = load_pickle(DATA_DIR+'/i2'+pickle_last_nm+'.pickle')
    angle = load_pickle(DATA_DIR+'/angle'+pickle_last_nm+'.pickle')
    sele_dangle = load_pickle(DATA_DIR+'/sele_dangle'+pickle_last_nm+'.pickle')
    cele_dangle = load_pickle(DATA_DIR+'/cele_dangle'+pickle_last_nm+'.pickle')
    th_svpwm = load_pickle(DATA_DIR+'/th_svpwm'+pickle_last_nm+'.pickle')
    i_svpwm = load_pickle(DATA_DIR+'/i_svpwm'+pickle_last_nm+'.pickle')
    th_er = load_pickle(DATA_DIR+'/th_er'+pickle_last_nm+'.pickle')
    th_cum = load_pickle(DATA_DIR+'/th_cum'+pickle_last_nm+'.pickle')
    pwm1 = load_pickle(DATA_DIR+'/pwm1'+pickle_last_nm+'.pickle')
    pwm2 = load_pickle(DATA_DIR+'/pwm2'+pickle_last_nm+'.pickle')

    t = np.linspace(0, i1.shape[0]-1, i1.shape[0]) * DELTA_T

    plt.figure(figsize=(20, 12))
    plt.plot(t, i1)
    plt.plot(t, i2)
    plt.xlabel('t', fontsize=24)
    plt.ylabel('A', fontsize=24)
    plt.title('phase A B current', fontsize=28)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.legend(['i1', 'i2'], fontsize=20)
    plt.savefig(FIG_DIR + '/i1_i2' + pickle_last_nm + '.png')

    plt.figure(figsize=(20, 12))
    plt.plot(t, angle)
    plt.xlabel('t', fontsize=24)
    plt.ylabel('angle coding', fontsize=24)
    plt.title('angle coding', fontsize=28)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.savefig(FIG_DIR + '/angle' + pickle_last_nm + '.png')

    plt.figure(figsize=(20, 12))
    plt.plot(t, sele_dangle)
    plt.plot(t, cele_dangle)
    plt.xlabel('t', fontsize=24)
    plt.ylabel('degree', fontsize=24)
    plt.title('command and sensor eletrical degree', fontsize=28)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.legend(['sensor', 'command'], fontsize=20)
    plt.savefig(FIG_DIR + '/scele_dangle' + pickle_last_nm + '.png')

    plt.figure(figsize=(20, 12))
    plt.plot(t, th_svpwm)
    plt.xlabel('t', fontsize=24)
    plt.ylabel('degree', fontsize=24)
    plt.title('theta svpwm', fontsize=28)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.savefig(FIG_DIR + '/th_svpwm' + pickle_last_nm + '.png')

    plt.figure(figsize=(20, 12))
    plt.plot(t, i_svpwm)
    plt.xlabel('t', fontsize=24)
    plt.ylabel('A', fontsize=24)
    plt.title('i svpwm', fontsize=28)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.savefig(FIG_DIR + '/i_svpwm' + pickle_last_nm + '.png')

    plt.figure(figsize=(20, 12))
    plt.plot(t, th_er)
    plt.xlabel('t', fontsize=24)
    plt.ylabel('degree', fontsize=24)
    plt.title('theta error', fontsize=28)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.savefig(FIG_DIR + '/th_er' + pickle_last_nm + '.png')

    plt.figure(figsize=(20, 12))
    plt.plot(t, th_cum)
    plt.xlabel('t', fontsize=24)
    plt.ylabel('degree', fontsize=24)
    plt.title('theta error accumulate', fontsize=28)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.savefig(FIG_DIR + '/th_cum' + pickle_last_nm + '.png')

    plt.figure(figsize=(20, 12))
    plt.plot(t, pwm1)
    plt.xlabel('t', fontsize=24)
    plt.ylabel('duty', fontsize=24)
    plt.title('1A1B PWM', fontsize=28)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.savefig(FIG_DIR + '/pwm1' + pickle_last_nm + '.png')

    plt.figure(figsize=(20, 12))
    plt.plot(t, pwm2)
    plt.xlabel('t', fontsize=24)
    plt.ylabel('duty', fontsize=24)
    plt.title('2A2B PWM', fontsize=28)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.savefig(FIG_DIR + '/pwm2' + pickle_last_nm + '.png')

    plt.figure(figsize=(20, 12))
    plt.plot(t, pwm1)
    plt.plot(t, pwm2)
    plt.xlabel('t', fontsize=24)
    plt.ylabel('duty', fontsize=24)
    plt.title('1A1B 2A2B PWM', fontsize=28)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.legend(['pwm1', 'pwm2'], fontsize=20)
    plt.savefig(FIG_DIR + '/pwm1_pwm2' + pickle_last_nm + '.png')

    print("===== sensor ele angle =====")
    print("max: ", np.max(sele_dangle))
    print("min: ", np.min(sele_dangle))
    print("mean: ", np.mean(sele_dangle))

    print("===== command ele angle =====")
    print("max: ", np.max(cele_dangle))
    print("min: ", np.min(cele_dangle))
    print("mean: ", np.mean(cele_dangle))

    print("===== theta error =====")
    print("max: ", np.max(th_er))
    print("min: ", np.min(th_er))
    print("mean: ", np.mean(th_er))
    print("machanical angle res: ", np.max(th_er)*1.8/90, np.min(th_er)*1.8/90)
    print("N_STEP: ", 1.8/(np.max(th_er)*1.8/90), 1.8/(np.min(th_er)*1.8/90))

    print("===== theta cum =====")
    print("max: ", np.max(th_cum))
    print("min: ", np.min(th_cum))
    print("mean: ", np.mean(th_cum))
