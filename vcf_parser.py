import vcf
import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image
from io import StringIO 

st.write("VCF Parser")
st.header("Select VCF File")
uploaded_file = st.file_uploader("VCF File", type=['vcf'], accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None)
# stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
# st.write(stringio)

# vcf_reader = vcf.Reader(open(uploaded_file))
# print(bytes_data)
if uploaded_file is not None:
	stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
	name = uploaded_file.name
	vcf_reader = vcf.Reader(stringio)

	translocation_records = []

	for record in vcf_reader:
	 	if record.INFO['SVTYPE'] == 'BND':
	 		st.write(record)
	 		translocation_records.append(record)

# print(len(translocation_records))
	