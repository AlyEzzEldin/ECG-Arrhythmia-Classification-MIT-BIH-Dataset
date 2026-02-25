import wfdb

# List of record numbers to load
record_numbers = ['100', '101', '102']
base_path = 'mit-bih-arrhythmia-database-1.0.0/'  # change to your actual extraction path

for rec in record_numbers:
    print(f"\n--- Record {rec} ---")
    
    # Load the record
    record = wfdb.rdrecord(base_path + rec)
    
    # ECG signal data
    signals = record.p_signal
    
    # Metadata
    sampling_freq = record.fs
    channel_names = record.sig_name
    duration = len(signals) / sampling_freq  # in seconds
    
    print(f"Sampling Frequency: {sampling_freq} Hz")
    print(f"Channel Names: {channel_names}")
    print(f"Recording Duration: {duration:.2f} seconds")
