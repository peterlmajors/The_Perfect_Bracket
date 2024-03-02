

def standard_scale(features, df_train, df_val, df_test=None):    
    mm = MinMaxScaler() 
    
    df_train[features] = pd.DataFrame(mm.fit_transform(df_train[features]), columns = features)
    df_val[features] = pd.DataFrame(mm.transform(df_val[features]), columns = features)
    
    if df_test is not None:
        df_test[features] = pd.DataFrame(mm.transform(df_test[features]), columns = features)
    
    return df_train, df_val, df_test