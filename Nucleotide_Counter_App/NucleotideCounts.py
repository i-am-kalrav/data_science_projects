import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image as img

i1 = img.open('DNA_Structure.jpg')

st.image(i1, use_column_width=True)

st.write("""
# DNA Nucleotide Count App
This app is for getting the counts of each nucleotide in the provided DNA sequence.
""")

st.subheader('DNA Sequence')
DNA_input = "GAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"
DNA = st.text_area(" Enter here:", DNA_input.upper(), height=100)
DNA = DNA.splitlines()
DNA = ''.join([line for line in DNA if line != 'empty'])

st.write("""###### DNA sequence input:""")
DNA


dct = dict([('A', DNA.count('A')), ('T', DNA.count('T')), ('G', DNA.count('G')), ('C', DNA.count('C'))])
#dct


i2 = img.open('Nucleotides.jpg')

st.image(i2, use_column_width=True)


st.write("""#### Nucleotide counts:""")
df = pd.DataFrame.from_dict(dct, orient='index')
df = df.rename({0:'Count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'Nucleotide' : 'Count'})
st.write(df)
#st.write(df.columns)


st.write("""#### Bar chart of the Nucleotide counts""")
p = alt.Chart(df).mark_bar().encode(
    x='index',
    y='Count'
)
p = p.properties(
    width=alt.Step(80)  # controls width of bar.
)
st.write(p)
