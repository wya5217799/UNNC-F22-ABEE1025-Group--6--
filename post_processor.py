import pandas as pd
import datatime as dt
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

#数据处理方法
#调整this_df数据
#具体方法我也不知道（要看数据）
def eplus_to_datetime(data_str):
    if data_str[-8:-6] != '24':
        dt_obj = pd.to_datetime(data_str)
    else:
        data_str = data_str[0:-8] + '00' + data_str[-6:]
        dt_obj = pd.to_datetime(data_str) + dt.time
    return dt_obj

#输入参数展示
# output_paths = run_one_parameter_parametric(eplus_run_path,idf_path,output_dir,
            # parameter_key,parameter_vals)

# plot_column_name = 'ZONE ONE:Zone Mean Air Temperature [C](TimeStep)'

# y_axis_title = 'Indoor Air Temperature (C)'

# plot_title = 'Simulation of Indoor Air Temprature vs. SHGC'

def plot_iD_results(output_paths, plot_column_name, y_axis_title, plot_title):
    fig, axs = plt.subplots(1,1, figsize=(20,10))
    fontsize = 20
    for this_path in output_paths:
        this_df = pd.read_csv(this_path)
        this_df['Date/Time'] = '2002' + this_df['Date/Time']
        this_df['Date/Time'] = this_df['Date/Time'].apply(eplus_to_datetime)
        data_st_date = this_df.iloc[0]['Date/Time']
        data_ed_date = this_df.iloc[-1]['Date/Time']
        data_list = this_df['Date/Time']
        this_y = this_df[plot_column_name].values
        # axs.plot(data_list,this_y...)#我也不到咋画
        #我再想想
        