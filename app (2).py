import numpy as np
import pandas as pd
import streamlit as st

st.title("NumPy Student Marks")
st.write("Enter marks separated by commas to calculate the mean, median, maximum, minimum and standard deviation with NumPy.")

default_text = "78, 85, 62, 90, 71, 89, 70, 65, 92, 55"
user_text = st.text_input("Marks", value=default_text)

values = []
invalid = []
for item in user_text.split(","):
    item = item.strip()
    if item == "":
        continue
    try:
        values.append(float(item))
    except ValueError:
        invalid.append(item)

if invalid:
    st.warning("Ignored invalid values: " + ", ".join(invalid))

out_of_range = [v for v in values if v < 0 or v > 100]
if out_of_range:
    st.warning("Marks should be between 0 and 100. Out of range values: " + ", ".join(str(v) for v in out_of_range))

if len(values) == 0:
    st.error("Please enter at least one valid number.")
else:
    marks = np.array(values)

    c1, c2, c3 = st.columns(3)
    c1.metric("Mean", f"{np.mean(marks):.2f}")
    c2.metric("Median", f"{np.median(marks):.2f}")
    c3.metric("Standard deviation", f"{np.std(marks):.2f}")
    c4, c5 = st.columns(2)
    c4.metric("Maximum", f"{np.max(marks):g}")
    c5.metric("Minimum", f"{np.min(marks):g}")

    if len(marks) > 1:
        st.write(f"Sample standard deviation (ddof=1): {np.std(marks, ddof=1):.2f}")

    st.header("Marks")
    df = pd.DataFrame({"Student": [f"Student {i + 1}" for i in range(len(marks))], "Marks": marks})
    st.bar_chart(df.set_index("Student")["Marks"])

    above = marks[marks > np.mean(marks)]
    st.write(f"Students above the mean: {len(above)} of {len(marks)}")

    st.header("Explanation")
    st.write(
        f"The mean is {np.mean(marks):.2f} and the median is {np.median(marks):.2f}. "
        f"The standard deviation of {np.std(marks):.2f} shows how spread out the marks are around the mean."
    )
