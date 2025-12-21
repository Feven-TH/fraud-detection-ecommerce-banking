import pandas as pd
import numpy as np
import pytest
from sklearn.preprocessing import StandardScaler

def test_time_diff_calculation():
    """Verify that signup-to-purchase time calculation is accurate."""
    data = {
        'signup_time': ['2025-01-01 10:00:00', '2025-01-01 10:00:00'],
        'purchase_time': ['2025-01-01 10:00:01', '2025-01-01 11:00:00']
    }
    df = pd.DataFrame(data)
    df['signup_time'] = pd.to_datetime(df['signup_time'])
    df['purchase_time'] = pd.to_datetime(df['purchase_time'])
    
    df['time_diff'] = (df['purchase_time'] - df['signup_time']).dt.total_seconds()
    
    assert df.loc[0, 'time_diff'] == 1.0  
    assert df.loc[1, 'time_diff'] == 3600.0

def test_velocity_logic():
    """Ensure the count of transactions per device is correctly computed."""
    data = {'device_id': ['DEV01', 'DEV01', 'DEV01', 'DEV02']}
    df = pd.DataFrame(data)
    
    # Logic: Group and count occurrences
    df['device_usage_count'] = df.groupby('device_id')['device_id'].transform('count')
    
    assert df.loc[0, 'device_usage_count'] == 3
    assert df.loc[3, 'device_usage_count'] == 1

def test_scaling_consistency():
    """Verify that StandardScaler maintains the relative order of features."""
    data = {'purchase_value': [10.0, 50.0, 100.0]}
    df = pd.DataFrame(data)
    
    scaler = StandardScaler()
    scaled_values = scaler.fit_transform(df[['purchase_value']])

    assert scaled_values[0] < scaled_values[1] < scaled_values[2]