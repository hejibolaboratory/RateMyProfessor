# -*- coding: UTF-8 -*-
'''
https://zhuanlan.zhihu.com/p/163927661
'''
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)


rootfolder=r'C:\Users\zhusx\Desktop\Courses\Python-Streamlit'
relativepath="."

#file_list=[relativepath+"\\"+"students%s.csv"%count for count in range(1,240)]
file_list=[relativepath+"\\"+"students%s.csv"%count for count in range(1,10)]


print(file_list)
 
main_dataframe = pd.DataFrame(pd.read_csv(file_list[0]))
 
for i in range(1,len(file_list)):
    data = pd.read_csv(file_list[i])
    df = pd.DataFrame(data)
    main_dataframe = pd.concat([main_dataframe,df],axis=1)
#print(main_dataframe)
data=main_dataframe

print(data[:100])
# 展示文本；文本直接使用Markdown语法
st.markdown("# Streamlit示例RateMyProfessor")


# 展示pandas数据框
#st.dataframe(pd.DataFrame([[1, 2], [3, 4]], columns=["a", "b"]))

# 展示matplotlib绘图
arr = np.random.normal(1, 1, size=100)
plt.hist(data["star_rating"], bins=20)
plt.title("matplotlib plot")
st.pyplot()