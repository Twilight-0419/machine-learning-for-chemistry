from typing import Tuple, Union
import numpy as np
import pandas as pd

R = 8.314    # ideal gas constant
KCAL_TO_KJ = 4.184    # energy unit conversion

def prepare_data(in_df: pd.DataFrame, temperature: float=298.0) -> Tuple[pd.DataFrame, pd.Series]:
    def calculate_c_x(x,row):
        if x == 'd':
            return np.exp(-row['e_pi_d']/(R*temperature/4184))/(np.exp(-row['e_pi_d']/(R*temperature/4184))+np.exp(-row['e_pi_D']/(R*temperature/4184)))
        elif x == 'D':
            return np.exp(-row['e_pi_D']/(R*temperature/4184))/(np.exp(-row['e_pi_d']/(R*temperature/4184))+np.exp(-row['e_pi_D']/(R*temperature/4184)))

    c_d = in_df.apply(lambda row: calculate_c_x('d', row), axis=1)
    c_D = in_df.apply(lambda row: calculate_c_x('D', row), axis=1)

    d_pi_w = c_d * in_df['d_pi_d'] + c_D * in_df['d_pi_D']
    e_pi_w = c_d * in_df['e_pi_d'] + c_D * in_df['e_pi_D']
    de_pi_w=d_pi_w * e_pi_w
    results = pd.DataFrame({'L_Alk': in_df['L_Alk'], 'B1_Alk': in_df['B1_Alk'], 'B5_Alk': in_df['B5_Alk'], 'L_Ar': in_df['L_Ar'], 'B1_Ar': in_df['B1_Ar'], 'B5_Ar': in_df['B5_Ar'], 'd_pi_w': d_pi_w, 'e_pi_w': e_pi_w, 'de_pi_w': de_pi_w})

    delta_delta_G = -R*temperature*np.log(in_df['er(%)']/100)/4184
    delta_delta_G.name = 'delta_delta_G'

    return results, delta_delta_G

def normalize(
    X_train: Union[pd.DataFrame, np.array], X_test: Union[pd.DataFrame, np.array]
) -> Tuple[np.array, np.array]:
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    X_train_normalized = scaler.fit_transform(X_train)
    X_test_normalized = scaler.transform(X_test)
    return X_train_normalized, X_test_normalized